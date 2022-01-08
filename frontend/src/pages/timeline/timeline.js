import * as d3 from 'd3v4';
import moment from 'moment'

const top = 25
const right = window.innerWidth / 3
const bottom = 15
const left = 10
const w = window.innerWidth - right - left

const miniHeight = 60
var x1 = d3.scaleLinear()
  .range([0, w]);


function toUTC(d) {
  if(!d || !d.getFullYear)return 0;
  return Date.UTC(d.getFullYear(), d.getMonth(), d.getDate());
}

function daysBetween(d1,d2){
  let days = toUTC(d2) - toUTC(d1) || 0;
  return days / 24 / 60 / 60 / 1000;
}
export function makeTimeline(svgRef, start_time, end_time, callback) {
  console.log(start_time)
  const timeStart =   new Date(start_time)
  const timeEnd =  new Date(end_time)

  console.log("mmmmm", timeStart, timeEnd)

  if (!timeStart || ! timeEnd) return

  var x = d3.scaleTime()
    .range([0, w])
    .domain([timeStart, timeEnd]);

  var days = daysBetween(timeStart, timeEnd);
  var tFormat = "%b";
  var tTick = 'timeMonth';
  if (days < 3){
    tFormat = "%Hh";
    tTick = 'timeHour';
  } else if (days < 35) {
    tFormat = "%a";
    tTick = 'timeDay';
  }

  var xAxis = d3.axisBottom(x)
      .ticks(d3[tTick])
      .tickFormat(d=>d3.timeFormat(tFormat)(d))

  let timeout = null

  function brushed() {
    var timeSelection = d3.event.selection.map(x.invert, x)

    if (!timeout) {
      timeout = true
    } else {
      clearTimeout(timeout)
      timeout = setTimeout(callback.bind(null, timeSelection[0], timeSelection[1]), 500)
    }
  }


  svgRef
    .select(".x-axis")
    .attr("transform", "translate(5, 35)")
    .call(xAxis)

  var brush = d3.brushX()
    .extent([[0, 0], [w, miniHeight]])
    .on("brush", brushed)

  svgRef.select(".brush")
    .attr("class", "x brush")
    .call(brush)
    .style("transform", `translateX(5px)`)
    .call(brush.move, x1.range())

}
