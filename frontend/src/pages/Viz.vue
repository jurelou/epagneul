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

    <q-dialog v-model="dialog_rankings" position="left">
      <q-card>

        <q-card-section class="row items-center no-wrap">
          <q-table
            title="Ranks per user"
            :rows="users"
            :columns="users_table_columns"
            row-key="name"
            @row-click="click_row"
          />

        </q-card-section>
      </q-card>
    </q-dialog>

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
              <q-btn
                outline
                rounded 
                style="width: 100%"
                color="primary"
                label="See rankings"
                @click="dialog_rankings = true"
              />

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
                      use-input
                      outlined
                      :options="available_search_users_ref"
                      v-model="selected_user"
                      
                      label="Search for a user"
                      input-debounce="0"
                      transition-show="scale"
                      transition-hide="scale"
                      @update:model-value="zoomNode($event, 'User')"
                      @filter="filterUser"
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
                      @update:model-value="zoomNode($event, 'Machine')"
                      @filter="filterMachine"
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


              <q-separator inset dark />

              <q-card-section>
                <div class="q-pa-md">
                  <q-btn-group spread>
                    <q-btn 
                      color="positive"
                      label="Select all" 
                      @click="select_all_relationships"/>
                    <q-btn 
                      color="negative"
                      label="Remove all"
                      @click="remove_all_relationships" />

                  </q-btn-group>
                </div>
                <q-option-group
                  v-model="default_viz_node_options"
                  :options="viz_node_options"
                  color="primary"
                  type="toggle"
                />
              </q-card-section>



          </q-card>
        </q-scroll-area>

        <q-card class="column">
          <q-card-section>
            <q-uploader
              :url="api_base_url + '/folders/' + route.params.folder + '/upload'"
              multiple
              @uploaded="uploaded_files"
              @failed="failed_upload_file"
            />
          </q-card-section>
        </q-card>


    </q-drawer>


        <!--
                            <q-item v-for="file in folder?.files" :key="file.identifier">
                              <q-item-section>
                                <q-item-label>{{ file.name }}</q-item-label>
                                <q-item-label caption lines="2">{{ file.timestamp }}</q-item-label>
                              </q-item-section>
                            </q-item>
    -->

    <div ref="resizeRef" class="timeline-main">
      <svg ref="svgRef" class="timeline-svg">
        <g class="x-axis" />
        <g class="brush" />
      </svg>
    </div>

    <div id="cy" />

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


const dialog_rankings = ref(false)
const route = useRoute()
const $q = useQuasar()
var cy = null

function click_row(_, item) {
  zoomNode(item.label, "User")
}
const users_table_columns = [
  {
    name: "username",
    label: "Username",
    field: "label",
    sortable: true,
    align: 'right',

  },
  {
    name: "rank",
    label: "Rank",
    field: "rank",
    sortable: true

  }
]
const users = ref([])
const svgRef = ref(null);

onMounted(() => {
  const svg = d3.select(svgRef.value);
  cy = makeCytoscape(folder.value)

  watchEffect(() => {
    if (!folder.value || !folder.value.files.length) return

    cy.json({elements: folder.value})
    makePopper(cy)

    makeTimeline(svg, folder.value.start_time, folder.value.end_time, updateSelectedNodes)
    start_time = new Date(folder.value.start_time)
    end_time = new Date(folder.value.end_time)
    updateSelectedNodes(start_time, end_time)

    onChangeVisualisationMode(selected_viz_type.value, false)
  
    users.value = []
    folder.value.nodes.forEach(node => {
      if (node.data.category == "User") {
        users.value.push(node.data)
      }
    })

  })
})

///////////////////////////////////////////////////////////////
// UPDATE EDGES
///////////////////////////////////////////////////////////////
let start_time = null
let end_time = null

function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

function updateSelectedNodes(start, end) {
  console.log("update node selection")
  start_time = start
  end_time = end
  const start_time_date = (start.getTime() - start.getTimezoneOffset() * 60000) / 1000 | 0
  const end_time_date = (end.getTime() - end.getTimezoneOffset() * 60000) / 1000 | 0

  available_search_machines = []
  available_search_users = []


  cy.edges().forEach(edge => {
    const isInTimerange = !edge.data().timestamps.every(ts => {
      if (ts >= start_time_date && ts <= end_time_date) {
        return false
      }
      return true
    })

    const edge_label = edge.data().event_type 
    const edge_value = edge.data().value
    const isInFilter = default_viz_node_options.value.includes(edge.data().event_type.toString())

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
      if (node_category == "Machine")
        available_search_machines.push(node.data().label)
      else if (node_category == "User")
        available_search_users.push(node.data().label)
    }
  })
  available_search_machines = available_search_machines.filter(onlyUnique)
  available_search_users = available_search_users.filter(onlyUnique)

  onChangeVisualisationMode(selected_viz_type.value)
}

///////////////////////////////////////////////////////////////
// SELECT MACHINE
///////////////////////////////////////////////////////////////
var selected_machine = ref()
var available_search_machines = []

const available_search_machines_ref = ref(available_search_machines)

function zoomNode(node_label, category) {
  if (category == "User") {
    selected_machine.value = null
  } else if (category == "Machine") {
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

function filterMachine (val, update, abort) {
  update(() => {
    const needle = val.toLowerCase()
      available_search_machines_ref.value = available_search_machines.filter(v => v.toLowerCase().indexOf(needle) > -1)
  })
}


///////////////////////////////////////////////////////////////
// SELECT USER
///////////////////////////////////////////////////////////////
const selected_user = ref()
var available_search_users = []

const available_search_users_ref = ref(available_search_users)

function filterUser (val, update, abort) {
  update(() => {
    const needle = val.toLowerCase()
      available_search_users_ref.value = available_search_users.filter(v => v.toLowerCase().indexOf(needle) > -1)
  })
}

///////////////////////////////////////////////////////////////
// FOLDER DATA
///////////////////////////////////////////////////////////////
const { folder, isLoading, refetch, isError } = useFolder(route.params.folder);


///////////////////////////////////////////////////////////////
// SELECT EDGES
///////////////////////////////////////////////////////////////
const default_viz_node_options = ref([
  "Successfull logon",
  "TGS request",
  "NTLM request",
  "Network connection",
  "Logon w/ explicit credentials"
])

  
const viz_node_options = [
  { label: "Successfull logon", value: "Successfull logon" },
  { label: "Failed logon", value: "Failed logon" },
  { label: "TGT AES Request", value: "TGT AES Request" },
  { label: "TGT DES Request", value: "TGT DES Request" },
  { label: "TGT RC4 Request", value: "TGT RC4 Request" },

  { label: "TGT failed", value: "TGT failed" },
  { label: "TGS request", value: "TGS request" },
  { label: "NTLM request", value: "NTLM request" },
  { label: "Network connection", value: "Network connection" },
  { label: "Logon w/ explicit credentials", value: "Logon w/ explicit credentials" },
  { label: "Group add", value: "Group add" },
]

function select_all_relationships() {
  default_viz_node_options.value = [
    "Successfull logon",
    "Failed logon",
    "TGT AES Request",
    "TGT DES Request",
    "TGT RC4 Request",
    "TGT failed",
    "TGS request",
    "NTLM request",
    "Network connection",
    "Logon w/ explicit credentials",
    "Group add"
  ]
}

function remove_all_relationships() {
    default_viz_node_options.value = []
}

///////////////////////////////////////////////////////////////
// CHANGE LAYOUT
///////////////////////////////////////////////////////////////
const options = [ 'fcose', 'klay', 'cose-bilkent', 'breadthfirst', 'grid', 'circle'];
const selected_viz_type = ref('fcose');

function onChangeVisualisationMode(layout_name, animate = true) {
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
import { api_base_url } from '../config';

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
  fill: #7fc97f !important;
  height: 27px;
  fill-opacity: 1;
}

.domain, .tick line{
  /*fill: blue; */
  stroke: #7fc97f;
}

.tick text{
  fill: grey; 
}


</style>