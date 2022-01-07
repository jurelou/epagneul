<template>
  
  
  <q-page>

  <q-drawer 
      show-if-above
      side="left"
      behavior="desktop"
      elevated>

    <q-scroll-area style="height: 83%; max-width: 300px;">
        <q-card class="no-margin column full-height">
          <q-card-section v-if="folder?.files?.length">
            <div class="row no-wrap items-center">
              <div class="col text-h6 ellipsis">
                {{ folder.name }}
              </div>
              <div class="col-auto text-grey text-caption q-pt-md row no-wrap items-center">
                <!--<q-icon name="folder" />-->
                {{ folder.files.length }} File(s)
              </div>
            </div>
          </q-card-section>

          <q-card-section v-else>
            No files yet!
          </q-card-section>

          <q-card-section class="q-pt-none" v-if="folder?.files?.length">
            <div class="text-subtitle1">
              $・Italian, Cafe
            </div>
            <div class="text-caption text-grey">
              Started: {{ folder.start_time }}
            </div>
            <div class="text-caption text-grey">
              Ended: {{ folder.end_time }}
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
              <q-expansion-item switch-toggle-side popup icon="open_in_full" label="Filter edges">
                <q-separator />
                  <div class="q-pa-sm q-gutter-md">
                    <q-btn outline text-color="negative" label="unselect all" size="sm" @click="unselect_all_edges"/>
                    <q-btn outline color="positive" label="select all" size="sm" @click="select_all_edges"/>
                  </div>
                  <q-option-group
                    color="teal"  
                    :options="viz_node_options"
                    type="checkbox"
                    v-model="default_viz_node_options"
                    @update:model-value="select_viz_relationships"  
                  />
              </q-expansion-item>
          </q-card-section>

          <q-card-section>
              <q-expansion-item switch-toggle-side popup icon="open_in_full" label="Filter edges">
                <q-separator />
                  <div class="q-pa-sm q-gutter-md">
                    <q-btn outline text-color="negative" label="unselect all" size="sm" @click="unselect_all_edges"/>
                    <q-btn outline color="positive" label="select all" size="sm" @click="select_all_edges"/>
                  </div>
                  <q-option-group
                    color="teal"  
                    :options="viz_node_options"
                    type="checkbox"
                    v-model="default_viz_node_options"
                    @update:model-value="select_viz_relationships"  
                  />
              </q-expansion-item>
          </q-card-section>

        </q-card>


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


            <q-list>
            

              <q-expansion-item switch-toggle-side popup icon="open_in_full" label="Filter edges">
                <q-separator />
                <q-card>
                  <q-card-section>
                    <div class="q-pa-sm q-gutter-md">
                      <q-btn outline text-color="negative" label="unselect all" size="sm" @click="unselect_all_edges"/>
                      <q-btn outline color="positive" label="select all" size="sm" @click="select_all_edges"/>
                    </div>
                    <q-option-group
                      color="teal"  
                      :options="viz_node_options"
                      type="checkbox"
                      v-model="default_viz_node_options"
                      @update:model-value="select_viz_relationships"
                      
                    />
                  </q-card-section>
                </q-card>
              </q-expansion-item>
              <q-expansion-item switch-toggle-side popup icon="search" label="Search">
                <q-separator />
                <q-card>
                  <q-card-section>
                    <q-select
                      use-input
                      outlined
                      :options="available_search_users_ref"
                      v-model="selected_machine"
                      label="Search for a user"
                      input-debounce="0"
                      transition-show="scale"
                      transition-hide="scale"
                      @update:model-value="zoomNode"
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
                </q-card>
              </q-expansion-item>
            </q-list>

      -->




    </q-scroll-area>
        <q-card class="no-margin column" style="overflow: hidden;">
          <q-card-section class="toto">

            <div class="text-caption text-no-wrap text-bold text-justify q-mb-md">Upload a new file</div>
            <q-uploader
              :url="base_url + '/folders/' + route.params.folder + '/upload'"
              multiple
              style="max-width: 100%; overflow: hidden;"
              @uploaded="uploaded_files"
              @failed="failed_upload_file"
            />
          </q-card-section>
        </q-card>
    <!--
    <q-card style="width: 300px; overflow: hidden;">

          <q-card-section>
            <div class="text-caption text-no-wrap text-bold text-justify q-mb-md">Upload a new file</div>
            <q-uploader
              :url="base_url + '/folders/' + route.params.folder + '/upload'"
              multiple
              style="max-width: 100%; overflow: hidden;"
              @uploaded="uploaded_files"
              @failed="failed_upload_file"
            />


          </q-card-section> 
    </q-card>
    -->
    </q-drawer>

    <div id="cy" />


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
        <div class="q-pa-md q-gutter-sm text-negative">
          You don't have any files yet !
          <br>
          Click on 'Upload new files'
        </div>
    </q-inner-loading>

    <div class="q-pa-md q-gutter-sm" style="z-index:999;" v-if="!isLoading && folder?.files?.length">
      <div id="timeline_header" />
      <!--
      <q-btn  v-if="folder?.files?.length"  icon="info" color="primary" text-color="dark" :label="'Summary for ' + folder.name" @click="infobox = true"/>
      <div id="timeline" />
      -->
      <div id="timeline_footer" />
    </div>

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


</q-page>
</template>

<script setup>
import { onMounted, ref, watch  } from 'vue';
import { useRoute } from 'vue-router'
import { useFolder } from '../hooks';
import { useQuasar } from 'quasar'

import { makeCytoscape } from './cy/cytoscape'
import { makePopper } from './cy/events';

const route = useRoute()
const $q = useQuasar()
const tab = ref('files')
var cy = null

var timeline_chart = null

onMounted(() => {
  cy = makeCytoscape(folder.value)

})

const infobox = ref(false)
const infotab = ref('machines')


///////////////////////////////////////////////////////////////
// TIMELINE
///////////////////////////////////////////////////////////////
import { make_timeline_header, make_timeline_footer } from './timeline/timeline';

let timeline_data = []

///////////////////////////////////////////////////////////////
// SELECT MACHINE
///////////////////////////////////////////////////////////////
const selected_machine = ref()

let available_search_users = []
const available_search_users_ref = ref(available_search_users)

function zoomNode(node_label) {
  const node = cy.elements().filter(e => e.data('label') == node_label)

  cy.nodes().forEach(n => n.removeClass('highlight'))
  cy.edges().forEach(n => n.removeClass('highlight'))
  node.addClass('highlight')
  /*
  node.incomers().forEach(e => { e.addClass('highlight') })
  node.outgoers().forEach(e => { e.addClass('highlight') })
  */
  cy.animation({
    zoom: 1,
    center: {
      eles: node
    }
  }).play()
}

function filterMachine (val, update) {
  if (val === '') {
    update(() => {
      available_search_users_ref.value = available_search_users
    })
    return
  }
  update(() => { available_search_users_ref.value = available_search_users.filter(v => v.toLowerCase().indexOf(val.toLowerCase()) > -1) })
}

///////////////////////////////////////////////////////////////
// FOLDER DATA
///////////////////////////////////////////////////////////////
const { folder, isLoading, refetch, isError } = useFolder(route.params.folder);

watch(() => folder, (folder) => {
  let v = folder.value
  cy.json({elements: v})
  onChangeVisualisationMode(selected_viz_type.value, false)
  makePopper(cy)



  let start_time = new Date(Date.parse(folder.value.start_time))
  let end_time = new Date(Date.parse(folder.value.end_time))


  if (!end_time || !start_time) {
    console.log("NOPE") 
  }
  make_timeline_footer(start_time, end_time)

  let timerange = []
  let i = 0
  while (true) {
    const date = new Date(start_time.getTime() +  (i*60*60*1000))
    timerange.push(date)
    if (date > end_time) { break }
    if (i > 100000) {
      console.log("Verry long timeline ... ", i)
      break
    }
    i++
  }
  console.log(timerange)

  folder.value.nodes.forEach((node, index) => {
    if (node.data.category == "user") {
      available_search_users.push(node.data.label)
      /*
      let node_timeline = []
      
      node.data.timeline.forEach((item, index) => {
        node_timeline.push({
          value: item,
          starting_time: timerange[index],
          ending_time: timerange[index + 1],
        })
      })
      timeline_data.push({
        label: node.data.label,
          isIncluded: true,
          times: node_timeline
      })

      */

    }
  })

//make_timeline(timeline_data)

}, { deep: true })
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

function select_all_edges() {
  default_viz_node_options.value = ["4624", "4625", "4768", "4769", "4776", "4648", "4771" ]
  select_viz_relationships(default_viz_node_options.value)
}

function unselect_all_edges() {
  default_viz_node_options.value = []
  select_viz_relationships([])
}

function select_viz_relationships(selected_ids) {
  console.log(selected_ids)
  cy.edges().forEach(edge => {
    if (selected_ids.includes(edge.data().label))
      edge.style("display", "element")
    else
      edge.style("display", "none")
  })
  cy.nodes().forEach(n => n.style("display", "element"))
  cy.nodes().forEach(node => {
    if (node.tippy && node.connectedEdges(":visible").size() === 0) { node.style("display", "none") }
  })
  cy.nodes().forEach(node => {
    if (!node.tippy && node.descendants(":visible").length == 0) { node.style("display", "none") }
  })

  onChangeVisualisationMode(selected_viz_type.value)
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
.q-uploader {
  width: 280px;
  margin-left: 10px !important;
  margin-right: 10px !important;
}

.q-page-container {
  padding-left: 0px !important;
}

.q-drawer{
  top: 0 !important;
}
 
  body {
    overflow: hidden;
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
  /*
  TIMELINE
  */
#timeline {
  background-color: transparent;
  overflow-y: scroll;
  overflow-x: hidden;
  height: 400px;
}
#timeline_footer {
  z-index: 99999;
}
.footer {
  fill: blue;
}

.mini {
  fill: pink;
}

.main {
  background-color: blue;
  fill: blue;
}

.core-chart line {
  stroke: grey;
}

.core-labels text {
  text-anchor: end;
  fill: blue;
}

.domain, .tick line{
  /*fill: blue; */
  stroke: #20C20E;
}

.tick text{
  fill: red; 
}

.selection {
  fill: #20C20E !important;

}

</style>
