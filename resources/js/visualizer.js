
$(document).ready(function () {
    var svg = d3.select('svg');
    //svg.attr("viewBox", "0 0 300 300");
    var visualizer_root = svg.append("g");
    //visualizer_root.attr("width", 300);

    d3.json("api/event-timeline")
        .then(data => {
            //snowflake = new Snowflake("abc");
            //snowflake.render(visualizer_root, 10, 10);

            namey = new Namey("sehar");
            namey.render(visualizer_root, 50, 50);

            namey = new Namey("lindsey");
            namey.render(visualizer_root, 105, 50);

            namey = new Namey("shafaq");
            namey.render(visualizer_root, 160, 50);

            namey = new Namey("rahat");
            namey.render(visualizer_root, 215, 50);

            namey = new Namey("mehak");
            namey.render(visualizer_root, 270, 50);
        });
});
