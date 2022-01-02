import * as d3 from 'd3v4';

var now = Date.now();
var lanes = [];
var times = [];
var w = window.innerWidth
var real_height = 280
var h = 500
var m = [25, 150, 15, 105], //top right bottom left
    w = w - m[1] - m[3],
    h = h - m[0] - m[2],
    miniHeight = 50,//laneLength * 12 + 50,
    mainHeight = h - miniHeight - 50;

var chartWidth = w + m[1] + m[3];
var chartHeight = h + m[0] + m[2];

const cScale = d3.scaleSequential()
  .interpolator(d3.interpolate('yellow', 'red'))
  .domain([0,1]);

function toDays(d) {
    d = d || 0;
    return d / 24 / 60 / 60 / 1000;
  }
  
  function toUTC(d) {
    if(!d || !d.getFullYear)return 0;
    return Date.UTC(d.getFullYear(), d.getMonth(), d.getDate());
  }
  
  function daysBetween(d1,d2){
    return toDays(toUTC(d2)-toUTC(d1));
  }




 
  
  export function make_timeline(timeline_data) {
    console.log("!!!!", timeline_data)
    return
    function drawBrush(minExtent, maxExtent) {
        var visItems = items.filter(function(d) {return d.starting_time <  maxExtent && d.ending_time > minExtent;});
        var toolTipDateFormat = d3.timeFormat("%Y-%m");  
        var days = daysBetween(minExtent,maxExtent);
          
        var tFormat = "%Y-%B";
        var tTick = 'timeMonth';
        if (days < 3){
          tFormat = "%H";
          tTick = 'timeHour';
        } else if (days < 7){
          tFormat = "%a %H";
          tTick = 'timeDay';
        } else if (days < 35){
          tFormat = "%Y-%B";
          tTick = 'timeWeek';
        }
    
        var xAxisTop2 = d3.axisBottom(xTop)
          .ticks(d3[tTick])
          .tickFormat(d=>d3.timeFormat(tFormat)(d));
      
    
        x1.domain([minExtent, maxExtent])
        xTop.domain([minExtent, maxExtent])
        gXTop.call(xAxisTop2)
        gXTop.selectAll('.tick text')
          
          
        currentLine.attr("x1", x1(now)).attr("x2", x1(now)).attr("y1", 0).attr("y2", mainHeight);
    
        //update main item rects
        var rects = itemRects.selectAll("rect")
          .data(visItems, function(d) { return d.id; })
          .attr("x", function(d) {return x1(d.starting_time);})
          .attr("width", function(d) {return x1(d.ending_time) - x1(d.starting_time);});
    
        rects.enter().append("rect")
          .attr("class", function(d) {return "miniItem "+d.state;})
          .attr("fill", function(d) {return cScale(d.value)})
          .attr("x", function(d) {return x1(d.starting_time)})
          .attr("y", function(d) {return y1(d.lane+0.1);})
          .attr("width", function(d) {return x1(d.ending_time) - x1(d.starting_time);})
          .attr("height", function(d) {return y1(1-2* 0.1);})
    
        rects.exit().remove();
      }
    
      function brushed() {
          var selection = d3.event.selection;
          var timeSelection = selection.map(x.invert, x);
    
          var minExtent = timeSelection[0];
          var maxExtent = timeSelection[1];  
          drawBrush(minExtent, maxExtent);
    
      }
    
  
timeline_data.forEach((d, index) => {
    lanes.push(d.label)
    d.times.forEach(time => { time["lane"] = index})
    times.push(d.times)
  })
  var laneLength = lanes.length;
  var items = [].concat.apply([], times);
  items.forEach((v, index) => { v["id"] = index })
  
  var timeBegin = d3.min(items, function(d) { return d["starting_time"]; });
  var timeEnd = d3.max(items, function(d) { return d["ending_time"]; });

  var x = d3.scaleTime()
  .range([0, w])
  .domain([timeBegin, timeEnd]);

var xTop = d3.scaleTime()
  .range([0, w])
  .domain([timeBegin, timeEnd]);

var x1 = d3.scaleLinear()
  .range([0, w]);

var y1 = d3.scaleLinear()
  .range([0, mainHeight])
  .domain([0, laneLength])
 
var y2 = d3.scaleLinear()
  .range([0, miniHeight])
  .domain([0, laneLength])

var xAxis = d3.axisBottom(x)
  .ticks(d3.timeMonth)
  .tickFormat(d=>d3.timeFormat("%Y %B")(d));
  
var xAxisTop = d3.axisBottom(xTop)
	.ticks(d3.timeDay)
  .tickFormat(d=>d3.timeFormat("%Y-%m-%d")(d));


  //////////////////////////////////////////////////////
  // HEADER
  //////////////////////////////////////////////////////
  var header = d3.select("#timeline_header")
    .append("svg")
    .attr("width", chartWidth)
    .attr("height", 19)
    .append("g")
    .attr("class", "header");

  var gXTop = header.append("g")
    .attr("class", "axis topAxis")
    .attr("transform", "translate(" + m[3] + "," + 0 + ")")
    .attr("font-size", 20)
    .call(xAxisTop);

  //////////////////////////////////////////////////////
  // FOOTER
  //////////////////////////////////////////////////////
  var footer = d3.select("#timeline_footer")
    .append("svg")
    .attr("width", chartWidth)
    .attr("height", 100)
    .append("g")
    .attr("class", "footer");

  var mini = footer.append("g")
    .attr("transform", "translate(150,10)")
    .attr("width", 150)
    .attr("height", 100)
    .attr("class", "mini");

  var gX = footer.append("g")
    .attr("class", "base axis botAxis")
    .attr("transform", "translate(150,10)")
    .call(xAxis);


  //////////////////////////////////////////////////////
  // TIMELINE
  //////////////////////////////////////////////////////

  var chart = d3.select("#timeline")
    .append("svg")
    .attr("width", chartWidth)
    .attr("height", chartHeight)
    .attr("viewBox", "0 0 " + chartWidth + " " + chartHeight)
    .attr("preserveAspectRatio", "xMidYMid meet")
    .append("g")
    .attr("class", "timelinechartg");

  chart.append("defs").append("clipPath")
    .attr("id", "clip")
    .append("rect")
    .attr("width", w)
    .attr("height", mainHeight);

  
  var main = chart
    .append("g")
    .attr("transform", "translate(" + m[3] + "," + 0 + ")")
    .attr("width", w)
    .attr("height", 100)
    .attr("class", "main");

  
  var div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);
    
  var defs = main.append('svg:defs');  

  //main lanes and texts
  main.append("g")
    .attr("class", "core-chart")
    .selectAll(".laneLines")
    .data(items)
    .enter().append("line")
    .attr("x1", 0)
    .attr("y1", function(d) {return y1(d.lane);})
    .attr("x2", w)
    .attr("y2", function(d) {return y1(d.lane);})

  main.append("g")
    .attr("class", "core-labels")
    .selectAll(".laneText")
    .data(lanes)
    .enter().append("text")
    .text(function(d) {return d;})
    .attr("x", (-10))
    .attr("y", function(d, i) {
      return y1(i + .5);
    })
    .attr("dy", ".5ex")
    .attr("class", "laneText");

  var itemRects = main.append("g")
    .attr("clip-path", "url(#clip)");

  var currentLine = main.append('line')
    .attr('class', "currentLine")
    .attr("clip-path", "url(#clip)");

  var brush = d3.brushX()
    .extent([[0, 0], [w, miniHeight]])
    .on("brush", brushed);

  var gBrush = mini.append("g")
    .attr("class", "x brush")
    .call(brush)
    //.selectAll("rect")
    //.attr("y", 1)
    //.attr("height", miniHeight - 1)    
    .call(brush.move, x1.range());

}