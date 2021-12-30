<script setup>

import { onMounted, ref, watch  } from 'vue';
import * as d3 from 'd3v4';
import Timeline from 'components/Timeline.vue'


  var data = [    {
        "label": "vbouget",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },

    {
        "label": "johna",
        "isIncluded": true,
        "times": [
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-service-ex",
        "isIncluded": true,
        "times": [
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 7,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 8,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 7,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 7,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 7,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 7,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 7,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 6,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 8,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "avachon",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "ybenjamin",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "cesteve",
        "isIncluded": true,
        "times": [
            {
                "value": 0.5,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0.5,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "ngonzalez",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "prousseaux",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "system",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-service-rd",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-infra-dc-a",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-service-rd",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "adm-jbordes",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "svieille",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "dfay",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-service-ex",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-secu-wec",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-dmz-rdsgw",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "adm-jlaporte",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-service-fi",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "adm-jjung",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-service-pk",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-service-pk",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "ooookmail",
        "isIncluded": true,
        "times": [
            {
                "value": 0.8,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-admin-wks1",
        "isIncluded": true,
        "times": [
            {
                "value": 0.2,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-admin-wks2bis",
        "isIncluded": true,
        "times": [
            {
                "value": 0.5,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-01",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "mchatain",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-03",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-02",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "tpignol",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-04",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "yauriol",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-06",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-08",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 5,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "lchevrier",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-07",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-05",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "acherrier",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "mcueff",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "achaulet",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "adm-ybenjamin",
        "isIncluded": true,
        "times": [
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 4,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "tdasse",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-12",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-09bis",
        "isIncluded": true,
        "times": [
            {
                "value": 0.2,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-13",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-11",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-10",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "jmougin",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "cfilippi",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "dsegura",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-17",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "fcathala",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-16",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-14",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-18",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-19",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-21",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "svacc-sap",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-20",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-23",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "lboulet",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-22",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-24",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-admin-wks1bis",
        "isIncluded": true,
        "times": [
            {
                "value": 0.2,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-admin-wks2",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-02",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-01",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-03",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-06",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-04",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-07",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-05",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-09",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-08",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-12",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-10",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-11",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-13",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 3,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-18",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-16",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-17",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-14",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "bite",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-23lol",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-21",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-22",
        "isIncluded": true,
        "times": [
            {
                "value": 8,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 2,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-19",
        "isIncluded": true,
        "times": [
            {
                "value": 8,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 1,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-20",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep-wks-24",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "administrator",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "gic-calid",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "nevergonnaletyoudown",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "scep.corp\\adm-ybenjamin",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    },
    {
        "label": "adm-mbouille",
        "isIncluded": true,
        "times": [
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T11:54:16.000"),
                "ending_time": Date.parse("2021-12-09T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T12:54:16.000"),
                "ending_time": Date.parse("2021-12-09T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T13:54:16.000"),
                "ending_time": Date.parse("2021-12-09T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T14:54:16.000"),
                "ending_time": Date.parse("2021-12-09T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T15:54:16.000"),
                "ending_time": Date.parse("2021-12-09T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T16:54:16.000"),
                "ending_time": Date.parse("2021-12-09T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T17:54:16.000"),
                "ending_time": Date.parse("2021-12-09T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T18:54:16.000"),
                "ending_time": Date.parse("2021-12-09T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T19:54:16.000"),
                "ending_time": Date.parse("2021-12-09T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T20:54:16.000"),
                "ending_time": Date.parse("2021-12-09T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T21:54:16.000"),
                "ending_time": Date.parse("2021-12-09T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T22:54:16.000"),
                "ending_time": Date.parse("2021-12-09T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-09T23:54:16.000"),
                "ending_time": Date.parse("2021-12-10T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T00:54:16.000"),
                "ending_time": Date.parse("2021-12-10T01:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T01:54:16.000"),
                "ending_time": Date.parse("2021-12-10T02:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T02:54:16.000"),
                "ending_time": Date.parse("2021-12-10T03:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T03:54:16.000"),
                "ending_time": Date.parse("2021-12-10T04:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T04:54:16.000"),
                "ending_time": Date.parse("2021-12-10T05:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T05:54:16.000"),
                "ending_time": Date.parse("2021-12-10T06:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T06:54:16.000"),
                "ending_time": Date.parse("2021-12-10T07:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T07:54:16.000"),
                "ending_time": Date.parse("2021-12-10T08:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T08:54:16.000"),
                "ending_time": Date.parse("2021-12-10T09:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T09:54:16.000"),
                "ending_time": Date.parse("2021-12-10T10:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T10:54:16.000"),
                "ending_time": Date.parse("2021-12-10T11:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T11:54:16.000"),
                "ending_time": Date.parse("2021-12-10T12:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T12:54:16.000"),
                "ending_time": Date.parse("2021-12-10T13:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T13:54:16.000"),
                "ending_time": Date.parse("2021-12-10T14:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T14:54:16.000"),
                "ending_time": Date.parse("2021-12-10T15:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T15:54:16.000"),
                "ending_time": Date.parse("2021-12-10T16:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T16:54:16.000"),
                "ending_time": Date.parse("2021-12-10T17:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T17:54:16.000"),
                "ending_time": Date.parse("2021-12-10T18:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T18:54:16.000"),
                "ending_time": Date.parse("2021-12-10T19:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T19:54:16.000"),
                "ending_time": Date.parse("2021-12-10T20:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T20:54:16.000"),
                "ending_time": Date.parse("2021-12-10T21:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T21:54:16.000"),
                "ending_time": Date.parse("2021-12-10T22:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T22:54:16.000"),
                "ending_time": Date.parse("2021-12-10T23:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-10T23:54:16.000"),
                "ending_time": Date.parse("2021-12-11T00:54:16.000")
            },
            {
                "value": 0,
                "starting_time": Date.parse("2021-12-11T00:54:16.000"),
                "ending_time": Date.parse("2021-12-11T01:54:16.000")
            }
        ]
    }
]


/*
// https://jsfiddle.net/m6ueL79o/3/
onMounted(() => {
   return
  function brushed() {
    var selection = d3.event.selection;
    var timeSelection = selection.map(x.invert, x);

    var minExtent = timeSelection[0];
    var maxExtent = timeSelection[1];  

	drawBrush(minExtent, maxExtent);

  }



  var w = 500
  var h = 500
  var m = [25, 150, 15, 105], //top right bottom left
      w = w - m[1] - m[3],
      h = h - m[0] - m[2],
      miniHeight = 50,//laneLength * 12 + 50,
      mainHeight = h - miniHeight - 50;

  data.forEach((d, index) => {

      lanes.push(d.label)
      d.times.forEach(time => {
          time["lane"] = index;
      })
      times.push(d.times)

  })
console.log("=>", lanes)

  var laneLength = lanes.length;
  var items = [].concat.apply([], times);

    items.forEach((v, index) => {
        v["id"] = index
    })

  var timeBegin = d3.min(items, function(d) { return Date.parse(d["starting_time"])});
  var timeEnd = d3.max(items, function(d) { return Date.parse(d["ending_time"])});

   console.log("@@@@", timeBegin, timeEnd)

  //scales
  var x =  d3.scaleTime()
  .range([0, w])
  .domain([timeBegin, timeEnd]);
  var xTop =  d3.scaleTime()
  .range([0, w])
  .domain([timeBegin, timeEnd]);
  var x1 = d3.scaleLinear()
  .range([0, w]);
  var y1 = d3.scaleLinear()
  .range([0, mainHeight])
  .domain([0, laneLength]);
  var y2 = d3.scaleLinear()
  .range([0, miniHeight])
  .domain([0, laneLength]);

  var xAxis = d3.axisBottom(x)
  .ticks(d3.timeMonth)
  .tickFormat(d=>d3.timeFormat("%Y-%m")(d));
  
  var xAxisTop = d3.axisBottom(xTop)
	.ticks(d3.timeMonth)
  .tickFormat(d=>d3.timeFormat("%Y-%m-%d")(d));

  var scaleFactor = (1/(timeEnd - timeBegin)) * (w);

  var chartWidth = w + m[1] + m[3];
  var chartHeight = h + m[0] + m[2];

  var chart = d3.select("#timeline")
  .append("svg")
  .attr("width", chartWidth)
  .attr("height", chartHeight)
  .attr("viewBox", "0 0 "+chartWidth+" "+chartHeight)
  .attr("preserveAspectRatio", "xMidYMid meet")
  .append("g")
  .attr("class", "timelinechartg");


  chart.append("defs").append("clipPath")
    .attr("id", "clip")
    .append("rect")
    .attr("width", w)
    .attr("height", mainHeight);

  var main = chart.append("g")
  .attr("transform", "translate(" + m[3] + "," + m[0] + ")")
  .attr("width", w)
  .attr("height", mainHeight)
  .attr("class", "main");

  var mini = chart.append("g")
  .attr("transform", "translate(" + m[3] + "," + (mainHeight + m[0]) + ")")
  .attr("width", w)
  .attr("height", miniHeight)
  .attr("class", "mini");

  var gX = chart.append("g")
  .attr("class", "base axis")
  .attr("transform", "translate(" + m[3] + "," + (mainHeight + miniHeight) + ")")
  .call(xAxis);
  
  gX.selectAll('.tick text');
  
  var div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);
  
  
  var gXTop = chart.append("g")
  .attr("class", "axis")
  .attr("transform", "translate(" + m[3] + "," + 0 + ")")
  .attr("font-size", 20)
  .call(xAxisTop);
  
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
    .attr("stroke", "lightgray")


  main.append("g")
    .attr("class", "core-labels")
    .selectAll(".laneText")
    .data(lanes)
    .enter().append("text")
    .text(function(d) {return d;})
    .attr("x", (-m[1] + 10))
    .attr("y", function(d, i) {
    return y1(i + .5);
  })
    .attr("dy", ".5ex")
    .attr("text-anchor", "start")
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



})

*/
</script>

<template>
    <q-page>
      <Timeline :data="data"/>
    </q-page>
</template>

<style>

/*
.chart {
	shape-rendering: crispEdges;
}
*/

.timelinechart {
  /*width:100%;
	border: 1px solid red;*/
}

.timelinechart svg {
  width: 100%;
  /*border: 1px solid green;*/
}

.timelinechartg {}

.mini text {}

.main text {}

.axis {}

.miniItem {
  stroke-width: 6;
}

.miniItem.future {
  fill: #448875;
}

text.future {
  fill: #f7b363;
}


.brush .extent {
  stroke: #b6b8b9;
  fill: #57585b;
  fill-opacity: .365;
  stroke-width: .2;
}

.laneImg {
  border-radius: 25px;
}

.currentLine {
  stroke-width: 2;
}


.axis text {
  font-size: 12px;
}

.base.axis text {
  font-size: 10px;
}

.laneText {
  font-size: 12px;
}



div.tooltip {
  position: absolute;
  text-align: left;
  width: 120px;
  height: 28px;
  padding: 2px;
  font: 12px sans-serif;
  background: #ffffff;
  border: 0px;
  pointer-events: none;
}


.noselect {
  -webkit-touch-callout: none;
  /* iOS Safari */
  -webkit-user-select: none;
  /* Safari */
  -khtml-user-select: none;
  /* Konqueror HTML */
  -moz-user-select: none;
  /* Old versions of Firefox */
  -ms-user-select: none;
  /* Internet Explorer/Edge */
  user-select: none;
  /* Non-prefixed version, currently
                                  supported by Chrome, Opera and Firefox */
}


.selection{
  fill: #ffffff;
  stroke: #0072ce;
  stroke-width: 1.5px;
  fill-opacity: 0.5;
}

.currentLine{
  stroke: darkgrey;
}

</style>