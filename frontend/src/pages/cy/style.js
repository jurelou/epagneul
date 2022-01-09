import cytoscape from 'cytoscape';

export const style = cytoscape.stylesheet()
    .selector('node').css({
            "content": "data(label)",
            "background-opacity": "data(bg_opacity)",
            "background-color": "data(bg_color)",
            "border-color": "data(border_color)",

            "width": "data(width)",
            "height": "60",

            "background-clip": "none",
            "background-repeat": "no-repeat",
            //"border-style": "solid",
            "border-width": "data(border_width)",
            "text-valign": "center",

            "font-size": "20",
            "color": "#dee2e6",
            "text-outline-color": "black",
            "text-outline-width": 1
    })
    .selector('[shape]').css({
        "shape": "data(shape)"
    })
    .selector('node:selected').css({
        "border-width": 2,
        "background-opacity": 0.7,
        "background-color": "data(border_color)",
        "border-color": "green",
        "color": "black",
        "text-outline-width": 0        

    })
    .selector('node.highlight').css({
        "border-width": 2,
        "background-opacity": 0.7,
        "background-color": "data(border_color)",
        "border-color": "green",

        "color": "black",
        "text-outline-width": 0
    })
    .selector('edge').css({
            "color": "#dee2e6",
            "text-outline-color": "black",
            "text-outline-width": 1,

            "content": "data(event_type)",
            "font-size": "17",
            "curve-style": "bezier",
            "target-arrow-shape": "triangle",
            "width": 2,
            "line-color": "grey",
            "target-arrow-color": "grey",
        })
    .selector('edge:selected').css({
            "width": "3",
            "line-color": "green",
            "target-arrow-color": "green",
        })
    .selector('edge.highlight').css({
        "width": "3",
        "font-size": "20",
        "line-color": "green",
        "target-arrow-color": "green",
})