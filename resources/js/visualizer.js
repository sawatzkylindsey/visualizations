
$(document).ready(function () {
    var svg = d3.select('svg');
    var visualizer_root = svg.append("g");

    d3.json("api/event-timeline")
        .get(function (error, data) {
            visualizer_root.append("rect")
                .attr("x", 10)
                .attr("y", 10)
                .attr("width", 10)
                .attr("height", 10);
    });
});
