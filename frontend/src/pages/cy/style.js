import cytoscape from 'cytoscape';

export const style = cytoscape.stylesheet()
    .selector('node').css({
            "shape": "data(shape)",

            "content": "data(label)",
            "background-opacity": "data(bg_opacity)",
            "background-color": "data(border_color)",
            "border-color": "data(border_color)",

            "width": "data(width)",
            "height": "60",

            "background-clip": "none",
            "background-repeat": "no-repeat",
            "border-width": "data(border_width)",
            "text-valign": "center",

            "font-size": "20",
            "color": "#dee2e6",
            "text-outline-color": "black",
            "text-outline-width": 1
    })
    .selector('node:selected').css({
        "border-width": 2,
        "background-opacity": 0.7,
        "background-color": "data(border_color)",
        "border-color": "#7fc97f",
        "color": "black",
        "text-outline-width": 0,

        "font-weight": "bold"
    })
    .selector('node.highlight').css({
        "border-width": 2,
        "background-opacity": 0.7,
        "background-color": "data(border_color)",
        "border-color": "#7fc97f",

        "color": "black",
        "text-outline-width": 0,

        "font-weight": "bold"

    })
    .selector('edge').css({
        "shape": "data(shape)",

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
        "line-color": "#7fc97f",
        "target-arrow-color": "#7fc97f",
        "font-weight": "bold"

    })
    .selector('edge.highlight').css({
        "width": "3",
        "font-size": "20",
        "line-color": "#7fc97f",
        "target-arrow-color": "#7fc97f",
        "font-weight": "bold"
    })