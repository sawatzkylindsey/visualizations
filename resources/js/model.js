

class Snowflake {
    constructor(name) {
        this.name = name;
    }

    render(root, offset_x, offset_y) {
        let size = 50;
        let center = size / 2;
        root.append("line")
            .attr("x1", offset_x + center)
            .attr("y1", offset_y + 0)
            .attr("x2", offset_x + center)
            .attr("y2", offset_y + size)
            .attr("stroke", "black");
        let diagonal_x = Math.cos(30 * (Math.PI / 180)) * size / 2;
        let diagonal_y = Math.sin(30 * (Math.PI / 180)) * size / 2;
        root.append("line")
            .attr("x1", offset_x + center + diagonal_x)
            .attr("y1", offset_y + center - diagonal_y)
            .attr("x2", offset_x + center - diagonal_x)
            .attr("y2", offset_y + center + diagonal_y)
            .attr("stroke", "black");
        root.append("line")
            .attr("x1", offset_x + center - diagonal_x)
            .attr("y1", offset_y + center - diagonal_y)
            .attr("x2", offset_x + center + diagonal_x)
            .attr("y2", offset_y + center + diagonal_y)
            .attr("stroke", "black");
    }
}

class Namey {
    constructor(name) {
        this.name = name;
    }

    render(root, offset_x, offset_y) {
        let size = 50;
        let center = size / 2;
        root.append("line")
            .attr("x1", offset_x - 1)
            .attr("y1", offset_y + center + 0.75)
            .attr("x2", offset_x + size + 1)
            .attr("y2", offset_y + center + 0.75)
            .attr("stroke-width", 1)
            .attr("stroke", "#AA7942");

        var alpha_x = function (letter) {
            var l = "abcdefghijklmnopqrstuvwxyz".indexOf(letter);
            console.assert(l >= 0, "invalid letter '" + letter + "'.");
            return (size / 25) * l;
        };

        var colour_interpolation = d3.interpolateLab("#33691e", "#85CE86");
        var dampen_index = function (i) {
            return (2 / (1 + Math.exp(-0.5 * i))) - 1;
        };

        for (var index = 1; index < this.name.length; index++) {
            let x1 = alpha_x(this.name[index - 1]);
            let x2 = alpha_x(this.name[index]);
            let x_delta = Math.abs(x2 - x1);
            var path = d3.path();
            path.moveTo(offset_x + x1, offset_y + center);
            path.quadraticCurveTo(offset_x + Math.min(x1, x2) + (x_delta / 2), offset_y + center - ((x_delta * -((size - 2) / size)) + size + 2), offset_x + x2, offset_y + center);
            path.closePath();
            //console.log("index " + index + ", dampen " + dampen_index(index - 1));
            var colour = colour_interpolation((index - 1) / (this.name.length - 1));

            //if (index + 1 == this.name.length) {
            root.append("path")
                .attr("d", path)
                .attr("fill", colour)
                .attr("opacity", 1 - ((index - 1) / (this.name.length - 0)))
                .attr("stroke", colour);
        }
    }
}
