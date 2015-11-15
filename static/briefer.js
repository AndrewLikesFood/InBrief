$(document).ready(function () {
  var bubbleChart = new d3.svg.BubbleChart({
    supportResponsive: true,
    //container: => use @default
    size: 650,
    //viewBoxSize: => use @default
    innerRadius: 600 / 3.5, // used to be 3.5
    //outerRadius: => use @default
    radiusMin: 50,
    //radiusMax: use @default
    //intersectDelta: use @default
    //intersectInc: use @default
    //circleColor: use @default
    curCircle: 0,
    data: {
      items: [
        {text: "Allen", id: 0, count: "2"},
        {text: ".Net", id: 1, count: "382"},
        {text: "Php", id: 2, count: "170"},
        {text: "Ruby", id: 3, count: "123"},
        {text: "D", id: 4, count: "12"},
        {text: "Python", id: 5, count: "170"},
        {text: "C/C++", id: 6, count: "382"},
        {text: "Pascal", id: 7, count: "10"},
        {text: "Something", id: 8, count: "170"},
      ],
      eval: function (item) {return item.count;},
      classed: function (item) {return item.text.split(" ").join("");}
    },
    plugins: [
      {
        name: "central-click",
        options: {
          text: 
            [
              "<div style='height:100px;width:100px;'>0</div>",
              "<div style='height:100px;width:100px;'>1</div>",
              "<div style='height:100px;width:100px;'>2</div>",
              "<div style='height:100px;width:100px;'>3</div>",
              "<div style='height:100px;width:100px;'>4</div>",
              "<div style='height:100px;width:100px;'>5</div>",
              "<div style='height:100px;width:100px;'>6</div>",
              "<div style='height:100px;width:100px;'>7</div>",
              "<div style='height:100px;width:100px;'>8</div>"
            ]
          ,
          style: {
            "font-size": "12px",
            "font-style": "italic",
            "font-family": "Source Sans Pro, sans-serif",
            //"font-weight": "700",
            "text-anchor": "middle",
            "fill": "white"
          },
          attr: {dy: "65px"},
          centralClick: function() {
            alert("Here are more details!!");
          }
        }
      },
      {
        name: "lines",
        options: {
          format: [
            {// Line #0
              textField: "count",
              classed: {count: true},
              style: {
                "font-size": "28px",
                "font-family": "Source Sans Pro, sans-serif",
                "text-anchor": "middle",
                fill: "white"
              },
              attr: {
                dy: "0px",
                x: function (d) {return d.cx;},
                y: function (d) {return d.cy;}
              }
            },
            {// Line #1
              textField: "text",
              classed: {text: true},
              style: {
                "font-size": "14px",
                "font-family": "Source Sans Pro, sans-serif",
                "text-anchor": "middle",
                fill: "white"
              },
              attr: {
                dy: "20px",
                x: function (d) {return d.cx;},
                y: function (d) {return d.cy;}
              }
            }
          ],
          centralFormat: [
            {// Line #0
              style: {"font-size": "50px"},
              attr: {}
            },
            {// Line #1
              style: {"font-size": "30px"},
              attr: {dy: "40px"}
            }
          ]
        }
      }]
  });
});