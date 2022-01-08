<template>
  
  
  <q-page>
    <q-inner-loading
        :showing="isLoading"
        label="Loading folder..."
        label-class="text-primary"
        color="primary"
        label-style="font-size: 1.1em"
        size="5.5em"
    />
    <q-inner-loading :showing="!isLoading && !folder?.files?.length">
        <q-spinner-radio size="5.5em" color="negative" />
        <div class="q-pa-md q-gutter-sm text-center text-negative">
          You don't have any files yet !
          <br>
          Click on the left panel to upload your files
        </div>
    </q-inner-loading>

  <q-drawer 
      show-if-above
      side="left"
      behavior="desktop"
      style="overflow: hidden; height: 100vh !important;"
      elevated>

        <q-scroll-area style="height: 79%; max-width: 300px;" v-if="folder?.files?.length">

          <q-card class="no-margin column full-height">
          <q-card-section>
              <div class="row no-wrap items-center">
                <div class="col text-h6 ellipsis">
                  {{ folder.name }}
                </div>
                <div class="col-auto text-grey text-caption q-pt-md row no-wrap items-center">
                  <!--<q-icon name="folder" />-->
                  {{ folder.files.length }} File(s)
                </div>
              </div>
              <!--
              <div class="text-subtitle1">
                $・Italian, Cafe
              </div>
              -->
              <div class="text-caption text-grey">
                Time range: {{ moment.duration(moment(folder.end_time).diff(moment(folder.start_time))).asDays().toFixed(1) }} days
              </div>
              <div class="text-caption">
                First event:
              </div>
              <div class="text-caption text-grey">
                {{ moment(folder.start_time).format("dddd, MMMM Do YYYY, h:mm:ss a") }}
              </div>
              <div class="text-caption">
                Last event:
              </div>
              <div class="text-caption text-grey">
                {{ moment(folder.end_time).format("dddd, MMMM Do YYYY, h:mm:ss a") }}
              </div>

            </q-card-section>

            <q-separator inset dark />

            <q-card-section>
                <!--<div class="text-caption text-no-wrap text-bold text-justify q-mb-md">aaa</div>-->
                      <q-select
                        label="Select layout"
                        transition-show="scale"
                        transition-hide="scale"
                        outlined
                        v-model="selected_viz_type"
                        :options="options"
                        @update:model-value="onChangeVisualisationMode" 
                      />

              </q-card-section>

              <q-separator inset dark />
              
              <q-card-section>

                <q-select
                  style="overflow: hidden;"
                  outlined
                  v-model="default_viz_node_options"
                  multiple
                  :options="viz_node_options"
                  use-chips
                  stack-label
                  label="Filter edges"
                  @update:model-value="select_viz_relationships"
                >

                  <template v-slot:selected-item="scope">
                    <q-chip
                      removable
                      dense
                      color="primary"
                      @remove="scope.removeAtIndex(scope.index)"
                    >
                      {{ scope.opt.value || scope.opt }}
                    </q-chip>
                  </template>

                </q-select>

              </q-card-section>


              <q-card-section>
                    <q-select
                      use-input
                      outlined
                      :options="available_search_users_ref"
                      v-model="selected_user"
                      label="Search for a user"
                      input-debounce="0"
                      transition-show="scale"
                      transition-hide="scale"
                      @update:model-value="zoomNode($event, 'user')"
                    >
                      <template v-slot:no-option>
                        <q-item>
                          <q-item-section class="text-grey">
                            No results
                          </q-item-section>
                        </q-item>
                      </template>
                    </q-select>    
              </q-card-section>

              <q-card-section>
                    <q-select
                      use-input
                      outlined
                      :options="available_search_machines_ref"
                      v-model="selected_machine"
                      label="Search for a machine"
                      input-debounce="0"
                      transition-show="scale"
                      transition-hide="scale"
                      @update:model-value="zoomNode($event, 'machine')"
                    >
                      <template v-slot:no-option>
                        <q-item>
                          <q-item-section class="text-grey">
                            No results
                          </q-item-section>
                        </q-item>
                      </template>
                    </q-select>    
              </q-card-section>

          </q-card>
        </q-scroll-area>

        <q-card class="column">
          <q-card-section>
            <q-uploader
              :url="base_url + '/folders/' + route.params.folder + '/upload'"
              multiple
              @uploaded="uploaded_files"
              @failed="failed_upload_file"
            />
          </q-card-section>
        </q-card>


    </q-drawer>


        <!--
        <q-separator />

             
              <q-expansion-item switch-toggle-side popup icon="description" label="Uploaded files" :caption="folder?.files?.length + ' files'">
                <q-separator />
                <q-card>
                  <q-card-section>
                        <q-list>
                            <q-item v-for="file in folder?.files" :key="file.identifier">
                              <q-item-section>
                                <q-item-label>{{ file.name }}</q-item-label>
                                <q-item-label caption lines="2">{{ file.timestamp }}</q-item-label>
                              </q-item-section>
                            </q-item>
                        </q-list>
                  </q-card-section>
                </q-card>
              </q-expansion-item>
    -->

    <div ref="resizeRef" class="timeline-main">
      <svg ref="svgRef" class="timeline-svg">
        <g class="x-axis" />
        <g class="brush" />
      </svg>
    </div>

    <div id="cy" />



    <!--
    <q-dialog v-model="infobox" >
      <q-card style="width: 900px; max-width: 800vw;">
        <q-card-section>
        <q-tabs
          v-model="infotab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
        >
          <q-tab name="machines" label="Machines" />
          <q-tab name="alarms" label="Alarms" />
          <q-tab name="movies" label="Movies" />
        </q-tabs>

        <q-separator />
        <q-tab-panels v-model="infotab" animated>
          <q-tab-panel name="machines">
            <div class="text-h6">machines</div>
              <div v-for="i in folder?.nodes" v-bind:key="i">
                {{ i }}
              </div>
          </q-tab-panel>

          <q-tab-panel name="alarms">
            <div class="text-h6">Alarms</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.sdqssssssssssssssss
          </q-tab-panel>

          <q-tab-panel name="movies">
            <div class="text-h6">Movies</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
        </q-tab-panels>
          

        </q-card-section>
      </q-card>
    </q-dialog>
  -->


</q-page>
</template>

<script setup>
import moment from 'moment'
import { onMounted, watchEffect, ref, watch  } from 'vue';
import { useRoute } from 'vue-router'
import { useQuasar } from 'quasar'

import { useFolder } from '../hooks';
import { makeCytoscape } from './cy/cytoscape'
import { makePopper } from './cy/events';
import { makeTimeline } from './timeline/timeline';

import * as d3 from 'd3v4';

const route = useRoute()
const $q = useQuasar()
var cy = null

const svgRef = ref(null);



onMounted(() => {
  const svg = d3.select(svgRef.value);
  cy = makeCytoscape(folder.value)

  if (folder.value && folder.value.files.length) {
    folder.value.nodes.forEach((node, index) => {
      if (node.data.category == "machine")
        available_search_machines_ref.value.push(node.data.label)
      else if (node.data.category == "user")
          available_search_users_ref.value.push(node.data.label)
    })
  }
  available_search_machines_ref.value = available_search_machines_ref.value.filter(onlyUnique)
  available_search_users_ref.value = available_search_users_ref.value.filter(onlyUnique)

  watchEffect(() => {
    if (!folder.value || !folder.value.files.length) return
    makeTimeline(svg, folder.value.start_time, folder.value.end_time, onChangeTimerange)
    start_time = new Date(folder.value.start_time)
    end_time = new Date(folder.value.end_time)

    cy.json({elements: folder.value})
    onChangeVisualisationMode(selected_viz_type.value, false)
    makePopper(cy)
  })
})

const infobox = ref(false)
const infotab = ref('machines')

///////////////////////////////////////////////////////////////
// UPDATE EDGES
///////////////////////////////////////////////////////////////
let start_time = null
let end_time = null

function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

function onChangeTimerange(start, end) {
  start_time = start
  end_time = end
  const start_time_date = (start.getTime() - start.getTimezoneOffset() * 60000) / 1000 | 0
  const end_time_date = (end.getTime() - end.getTimezoneOffset() * 60000) / 1000 | 0

  available_search_machines_ref.value = []
  available_search_users_ref.value = []


  cy.edges().forEach(edge => {
    const isInTimerange = !edge.data().timestamps.every(ts => {
      if (ts >= start_time_date && ts <= end_time_date) {
        return false
      }
      return true
    })

    const edge_label = edge.data().label 
    const edge_value = edge.data().value

    const isInFilter = !default_viz_node_options.value.every(i => {
      if (i === edge_label || i.value === edge_label) {
        return false
      }
      return true
    })

    if (isInFilter && isInTimerange) {
      edge.style("display", "element")
    } else {
      edge.style("display", "none")
    }
  
  })

  cy.nodes().forEach(n => {
    n.style("display", "element")
  })
  cy.nodes().forEach(node => {
    if (node.tippy && node.connectedEdges(":visible").size() === 0) { node.style("display", "none") }
  })
  cy.nodes().forEach(node => {
    if (!node.tippy && node.descendants(":visible").length == 0) { node.style("display", "none") }
  })

  cy.nodes().forEach(node => {
    if (node.style().display == "element"){
      const node_category = node.data().category
      if (node_category == "machine")
        available_search_machines_ref.value.push(node.data().label)
      else if (node_category == "user")
        available_search_users_ref.value.push(node.data().label)
    }
  })
  available_search_machines_ref.value = available_search_machines_ref.value.filter(onlyUnique)
  available_search_users_ref.value = available_search_users_ref.value.filter(onlyUnique)


  onChangeVisualisationMode(selected_viz_type.value)

}


///////////////////////////////////////////////////////////////
// SELECT MACHINE
///////////////////////////////////////////////////////////////
var selected_machine = ref()
const available_search_machines_ref = ref([])

function zoomNode(node_label, category) {
  if (category == "user") {
    selected_machine.value = null
  } else if (category == "machine") {
    selected_user.value = null
  }
  const node = cy.nodes().filter(e => e.data('label') == node_label && e.data('category') == category)
  cy.nodes().forEach(n => n.removeClass('highlight'))
  cy.edges().forEach(n => n.removeClass('highlight'))
  node.addClass('highlight')

  node.incomers().forEach(e => { e.addClass('highlight') })
  node.outgoers().forEach(e => { e.addClass('highlight') })

  cy.animation({
    zoom: 1,
    center: {
      eles: node
    }
  }).play()
}

///////////////////////////////////////////////////////////////
// SELECT USER
///////////////////////////////////////////////////////////////
const selected_user = ref()
const available_search_users_ref = ref([])

///////////////////////////////////////////////////////////////
// FOLDER DATA
///////////////////////////////////////////////////////////////
const { folder, isLoading, refetch, isError } = useFolder(route.params.folder);

///////////////////////////////////////////////////////////////
// SELECT EDGES
///////////////////////////////////////////////////////////////
const default_viz_node_options = ref(["4624", "4625", "4768", "4769", "4776", "4648", "4771" ])
const viz_node_options = [
  { label: '4624: Successful logon', value: '4624', color: 'green' },
  { label: '4625: Logon failure', value: '4625', color: 'green' },
  { label: '4648: Explicit credential logon', value: '4648', color: 'green' },
  { label: '4768: Kerberos Authentication (TGT)', value: '4768', color: 'green' },
  { label: '4769: Kerberos Service Ticket', value: '4769', color: 'green' },
  { label: '4776: NTLM Authentication', value: '4776', color: 'green' },
  { label: '4771: Kerberos pre-authentication failed', value: '4771', color: 'green' }
]

function select_viz_relationships(selected_ids) {
  default_viz_node_options.value = selected_ids
  onChangeTimerange(start_time, end_time)
}

///////////////////////////////////////////////////////////////
// CHANGE LAYOUT
///////////////////////////////////////////////////////////////
const options = [ 'fcose', 'cose-bilkent', 'breadthfirst', 'klay', 'grid', 'circle'];
const selected_viz_type = ref('fcose');

function onChangeVisualisationMode(layout_name, animate = true) {
  console.log("ANIMATE")
  cy.layout({
    name: layout_name,
    randomize: true,
    //animationEasing: 'ease-out-sine',
    animate: animate,
    animationDuration: 1000,

    fit: true,
    tile: true,
    idealEdgeLength: 80,
    packComponents: false,
    nodeRepulsion: 17000
  }).run()
}

///////////////////////////////////////////////////////////////
// FILE UPLOAD
///////////////////////////////////////////////////////////////
const base_url = process.env.VUE_APP_BASE_URL

function uploaded_files(info) {
  refetch.value()
}

function failed_upload_file(info) {
  console.log(info)
  $q.notify({
    type: 'negative',
    message: JSON.parse(info.xhr.response).errors[0]
  })
}


</script>

<style>

body {
  overflow: hidden;
}
.q-uploader {
  width: 250px;
  margin-left: 10px;
  margin-right: 10px;
}

.q-page-container {
  padding-left: 0px !important;
}

.q-drawer{
  top: 0 !important;
}
  
#cy {
  position: absolute;
  left: 300px;
  top: 0;
  bottom: 0;
  right: 0;
  margin-top: 5%;
  height: 95%;
}

.popper-div {
  position: relative;
  background-color: #333;
  color: #fff;
  border-radius: 4px;
  font-size: 14px;
  line-height: 1.4;
  outline: 0;
  padding: 5px 9px;
}

.cxtmenu-disabled {
	opacity: 0.333;
}

/* TIMELINE */

.timeline-main {
  width: 100%;
  height: 150px;
  margin-left: 29%;
}

.timeline-svg {
  width: 100%;
}

.brush {
  height: 100px;
}

.selection {
  fill: #20C20E !important;
  height: 30px;
  fill-opacity: .8;
}

.domain, .tick line{
  /*fill: blue; */
  stroke: #20C20E;
}

.tick text{
  fill: grey; 
}


</style>
