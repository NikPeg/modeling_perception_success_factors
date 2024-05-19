let simulation = null;

document.addEventListener("DOMContentLoaded", function() {

    const chart = (() => {
        const width = window.innerWidth;
        const height = window.innerHeight;
        const types = Array.from(new Set(suits.map(d => d.type))).sort();
        let nodes = factorsArray;
        const nodes_types = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1];

        const links = suits.map(d => Object.create(d));

        const color = d3.scaleOrdinal()
            .domain(types) // The categories you want to color
            .range(["#f76dc0", "#fa46b2", "#fc23a6", "#ff009a", "#e00288", "#b80270", "#870152"]);

        simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id).distance(300))
            .force("charge", d3.forceManyBody().strength(-400))
            .force("x", d3.forceX())
            .force("y", d3.forceY());

        const svg = d3.create("svg")
            .attr("viewBox", [-width / 2, -height / 2, width, height])
            .attr("width", width)
            .attr("height", height)
            .attr("style", "max-width: 100%; height: auto; font: 12px sans-serif;");

        svg.append("defs").selectAll("marker")
            .data(types)
            .join("marker")
            .attr("id", d => `arrow-${d}`)
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 15)
            .attr("refY", -0.5)
            .attr("markerWidth", 6)
            .attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path")
            .attr("fill", color)
            .attr("d", "M0,-5L10,0L0,5");

        const link = svg.append("g")
            .attr("fill", "none")
            .attr("stroke-width", 1.5)
            .selectAll("path")
            .data(links)
            .join("path")
            .attr("stroke", d => color(d.type))
            .attr("marker-end", d => `url(${new URL(`#arrow-${d.type}`, location)})`);

        const nodes_color = d3.scaleOrdinal()
            .domain(nodes_types)
            .range(["#81fcfc", "#68fcfc", "#49fcfc", "#21fcfc", "#03ffff", "#02f2f2", "#02dede", "#02c2c2", "#02abab", "#008c8c"]);

        const node = svg.append("g")
            .attr("stroke-linecap", "round")
            .attr("stroke-linejoin", "round")
            .selectAll("g")
            .data(nodes)
            .join("g")
            .attr("fill", d => {
                return nodes_color(d.value);
            })  // Use the color scale for fill
            .call(drag(simulation));

        node.append("circle")
            .attr("stroke", "none")
            // .attr("stroke-width", 1.5)
            .attr("r", 4);

        node.append("text")
            .attr("x", 8)
            .attr("y", "0.31em")
            .text(d => d.id)
            // .clone(true).lower()
            .attr("fill", "black")
            .attr("stroke", "black")
            .attr("stroke-width", 0.5);

        simulation.on("tick", () => {
            link.attr("d", linkArc);
            node.attr("transform", d => `translate(${d.x},${d.y})`);
        });

        return svg.node();
    })();

    document.body.appendChild(chart);
});

function drag(simulation) {
    function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }

    function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }

    function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }

    return d3.drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
}

function linkArc(d) {
    const r = Math.hypot(d.target.x - d.source.x, d.target.y - d.source.y);
    return `
                M${d.source.x},${d.source.y}
                A${r},${r} 0 0,1 ${d.target.x},${d.target.y}
            `;
}

// FCM processor
function processFCM(nodes, links, alpha=0.1, epsilon=0.5, steps=1000) {
    // Converting nodes array to a map for easy access.
    let nodeMap = nodes.reduce((map, node) => {
        map[node.id] = node.value;
        return map;
    }, {});

    // Function to get the updated value for a node
    function updateNodeValue(nodeId) {
        let newValue = nodeMap[nodeId];
        links.forEach(link => {
            if (link.target === nodeId) {
                newValue += alpha * link.type * nodeMap[link.source];
            }
        });
        return newValue;
    }

    // Function to check if the FCM has converged
    function hasConverged(oldValues, newValues) {
        return Object.keys(oldValues).every(nodeId => Math.abs(oldValues[nodeId] - newValues[nodeId]) <= epsilon);
    }

    let currentValues = {...nodeMap};
    let newValues = {...nodeMap};

    // Processing steps
    for (let step = 0; step < steps; step++) {
        newValues = Object.keys(nodeMap).reduce((map, nodeId) => {
            map[nodeId] = updateNodeValue(nodeId);
            return map;
        }, {});

        if (hasConverged(currentValues, newValues)) {
            break;
        }

        currentValues = {...newValues};
    }
    
    // Transform values to right format
    const transformedValues = Object.entries(newValues).map(([key, value]) => {
        return { "factor": key, "result value": value };
    });

    return transformedValues;
}

function shakeNodes() {
    // Get values from inputs
    const alpha = parseFloat(document.getElementById('AlphaInput').value);
    const epsilon = parseFloat(document.getElementById('EpsilonInput').value);
    const steps = parseInt(document.getElementById('StepsInput').value, 10) || 5000;

    const shakeIntensity = 5; // Adjust this for stronger or weaker shaking
    const shakeInterval = 100; // Interval in milliseconds for shaking

    function startShaking() {
        simulation.nodes().forEach(node => {
            node.fx = node.x + (Math.random() - 0.5) * shakeIntensity;
            node.fy = node.y + (Math.random() - 0.5) * shakeIntensity;
        });
        simulation.alpha(1).restart();
    }

    function stopShaking() {
        simulation.nodes().forEach(node => {
            node.fx = null;
            node.fy = null;
        });
        simulation.alphaTarget(0).restart();
    }

    const intervalId = setInterval(startShaking, shakeInterval);

    let newValues = processFCM(factorsArray, suits, alpha, epsilon, steps);
    setTimeout(() => {
        clearInterval(intervalId);
        stopShaking();
        alert("The algorithm for analyzing the fuzzy cognitive map has been completed successfully. Click OK to download the report.");

        // Trigger a download or any follow-up action
        downloadReport(newValues);
    }, steps);
}

function triggerShakeNodes() {
    // Get values from inputs
    const alpha = parseFloat(document.getElementById('AlphaInput').value);
    const epsilon = parseFloat(document.getElementById('EpsilonInput').value);
    const steps = parseInt(document.getElementById('StepsInput').value, 10);

    // Call shakeNodes with the obtained values
    shakeNodes(alpha, epsilon, steps);
}

function downloadReport(newValues) {
    const nodes = factorsArray;

    const nodes_worksheet = XLSX.utils.json_to_sheet([{ A: 'Factors:' }], { skipHeader: true }); // Without headers
    XLSX.utils.sheet_add_json(nodes_worksheet, nodes, { origin: -1 });

    // Create a new workbook and append the worksheet
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, nodes_worksheet, "Nodes");

    const links_worksheet = XLSX.utils.json_to_sheet([{ A: 'Links:' }], { skipHeader: true }); // Without headers
    XLSX.utils.sheet_add_json(links_worksheet, suits, { origin: -1 });
    XLSX.utils.book_append_sheet(workbook, links_worksheet, "Links");

    const result_worksheet = XLSX.utils.json_to_sheet([{ A: 'Result values:' }], { skipHeader: true }); // Without headers
    XLSX.utils.sheet_add_json(result_worksheet, newValues, { origin: -1 });
    XLSX.utils.book_append_sheet(workbook, result_worksheet, "Result values");

    // Generate binary string representation of the workbook
    const wbout = XLSX.write(workbook, { bookType: "xlsx", type: "binary" });

    // Function to convert binary string to an array buffer
    function s2ab(s) {
        var buf = new ArrayBuffer(s.length);
        var view = new Uint8Array(buf);
        for (var i = 0; i < s.length; i++) {
            view[i] = s.charCodeAt(i) & 0xFF;
        }
        return buf;
    }

    // Create a blob from the array buffer and create an object URL
    const blob = new Blob([s2ab(wbout)], { type: "application/octet-stream" });
    const url = URL.createObjectURL(blob);

    // Create a temporary anchor element to trigger the download
    const a = document.createElement("a");
    a.href = url;
    a.download = name + "-report.xlsx";
    document.body.appendChild(a);
    a.click();

    // Clean up
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
