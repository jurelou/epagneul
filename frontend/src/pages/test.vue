<script setup>

import { onMounted, ref, watch  } from 'vue';
import TimelinesChart from 'timelines-chart';
import * as d3 from 'd3';

const data = [
    {
        "group": "group1",
        "data": [
            {
                "label": "",
                "data": [
                    {
                        "timeRange": [
                            "2013-04-30T10:43:34.100",
                            "2013-06-07T20:12:51.066"
                        ],
                        "val": 0.8181930913383458
                    },
                    {
                        "timeRange": [
                            "2013-10-06T03:11:07.284Z",
                            "2013-10-30T23:01:34.869Z"
                        ],
                        "val": 0.1198978786407721
                    }
                ]
            }
        ]
    },
    {
        "group": "group2",
        "data": [
            {
                "label": "",
                "data": [
                    {
                        "timeRange": [
                            "2012-04-31T10:43:34.100Z",
                            "2013-06-09T20:12:51.066Z"
                        ],
                        "val": 0.8181930913383458
                    },
                    {
                        "timeRange": [
                            "2013-10-01T03:11:07.284Z",
                            "2013-10-02T23:01:34.869Z"
                        ],
                        "val": 0.1198978786407721
                    }
                ]
            }
        ]
    }
]

function onZoom(dates, pos) {    
    const [a, b] = dates
    console.log("!!!!", typeof(a))
}

onMounted(() => {
    var container = document.getElementById('timeline');

    const cScale = d3.scaleSequential()
        .interpolator(d3.interpolate('yellow', 'red'))
        .domain([0,1]);

    TimelinesChart()(container)
      //.xTickFormat(n => +n)
      //.zQualitative(true)
      //.dateMarker(new Date() - 365 * 24 * 60 * 60 * 1000) // Add a marker 1y ago      
      .zColorScale(cScale)
      .zScaleLabel("my skale")
      .sortChrono(true)
      .onZoom(onZoom)
      .data(data);

})

  
</script>

<template>
    <q-page>
    aaa
        <div id="timeline"></div>
    </q-page>
</template>

<style>


.tick {
        font: 10px sans-serif;
        font-family: "Roboto", "-apple-system", "Helvetica Neue", Helvetica, Arial, sans-serif;
}

.timelines-chart .axises .y-axis text, .timelines-chart .axises .grp-axis text {
    fill: red;
}

.timelines-chart .reset-zoom-btn {
    fill : yellow !important;
    opacity: 1 !important;
}
.legend rect {
    fill: rgba(0,0,0,0) !important;
    stroke-width: 0 !important;
}

.legend text {
    fill: rgba(100,100,140,0.0) !important;
}

.chart-tooltip {
  color: #20C20E !important;
  background: rgba(100,0,140,0.85) !important;
}

.chart-zoom-selection, .brusher .brush .selection {
  stroke: blue;
  fill: red;
  fill-opacity: 0.3;
}

.brusher {

  .grid-background {
    fill: lightgrey;
  }

  .axis path {
    display: none;
  }

  .tick text {
    text-anchor: middle;
    font: 100px sans-serif;
  }

  .grid {
    line, path {
      stroke: #fff;
    }
  }
}


</style>