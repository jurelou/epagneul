<template>
  <q-page >

    <p v-if="isLoading">Loading graph...</p>


    <q-banner v-if="!folder?.files?.length" inline-actions class="text-white bg-negative">
      There is no files !
    </q-banner>
    <div v-else class="q-pa-md q-gutter-sm">
      <q-btn icon="info" color="primary" text-color="dark" style="z-index:999;" label="Summary" @click="infobox = true"/>
    </div>


    <div id="cy" />
    
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



    <q-drawer 
      show-if-above
      side="right"
      behavior="desktop"
      elevated>

      <q-card>
        <q-tabs
          v-model="tab"
          dense
          align="justify"
          narrow-indicator
          indicator-color="primary"
          active-color="primary"
          class="text-grey-8"
        >
          <q-tab icon="description" name="files" label="files" />
          <q-tab icon="visibility" name="vizualisation" label="visualization" />
        </q-tabs>
        <q-separator />

        <!--
        FILES MGMT
        -->
        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="files">
            <q-list>
              <q-expansion-item switch-toggle-side popup default-opened icon="upload" label="Upload new files">
                <q-separator />
                <q-card>
                  <q-card-section>
                        <q-uploader
                          :url="base_url + '/folders/' + route.params.folder + '/upload'"
                          multiple
                          style="max-width: 100%"
                          @uploaded="uploaded_files"
                          @failed="failed_upload_file"
                        />
                  </q-card-section>
                </q-card>
              </q-expansion-item>
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
            </q-list>
          </q-tab-panel>

        <!--
        VIZ SETTINGS
        -->
          <q-tab-panel name="vizualisation">
            <q-list>

              <q-expansion-item style=" overflow: hidden;" switch-toggle-side popup icon="graph" label="Layout">
                <q-separator />
                <q-card>
                  <q-card-section>
                  <q-select
                    label="Layout type"
                    transition-show="scale"
                    transition-hide="scale"
                    outlined
                    v-model="selected_viz_type"
                    :options="options"
                    @update:model-value="onChangeVisualisationMode" 
                  />
                  </q-card-section>
                </q-card>
              </q-expansion-item> 

              <q-separator spaced />
              <q-item >
              <q-item-section>


                <q-option-group
                  color="teal"  
                  :options="viz_node_options"
                  type="checkbox"
                  v-model="default_viz_node_options"
                  @update:model-value="select_viz_relationships"
                  
                />
              
              </q-item-section>
              </q-item>
            </q-list>


            <div class="q-pa-md">
              <div class="q-px-sm">

              </div>
            </div>

          </q-tab-panel>

        </q-tab-panels>
      </q-card>
    </q-drawer>
</q-page>
</template>

<script setup>
import { onMounted, ref, watch  } from 'vue';
import { useRoute } from 'vue-router'
import { useFolder } from '../hooks';
import { useQuasar } from 'quasar'

import cytoscape from 'cytoscape';

import cxtmenu from 'cytoscape-cxtmenu';
import popper from 'cytoscape-popper';
import klay from 'cytoscape-klay';
import coseBilkent from 'cytoscape-cose-bilkent';
import fcose from 'cytoscape-fcose';
import layoutUtilities from 'cytoscape-layout-utilities';
import viewUtilities  from 'cytoscape-view-utilities';

import { style } from './cy/style';
import { makePopper, makeEvents } from './cy/events';

cytoscape.use( cxtmenu );
cytoscape.use( layoutUtilities );
cytoscape.use( viewUtilities );

cytoscape.use( popper );
cytoscape.use( klay );
cytoscape.use( coseBilkent );
cytoscape.use( fcose );


const route = useRoute()
const $q = useQuasar()
const { folder, isLoading, refetch, isError } = useFolder(route.params.folder);

var cy = null;
const base_url = process.env.VUE_APP_BASE_URL

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

const options = [ 'fcose', 'cose-bilkent', 'breadthfirst', 'klay', 'grid', 'circle'];
const selected_viz_type = ref('fcose');
const tab = ref('files');
const infobox = ref(false)
const infotab = ref('machines')

function layoutConfig(layout, animate = 'end') {
  return {
    name: layout,
    quality: 'proof',
    randomize: true,
    animationEasing: 'ease-in-sine',
    animate: animate,
    animationDuration: 1000,

    fit: true,
    tile: false,
    idealEdgeLength: 80,
    packComponents: false,
    nodeRepulsion: 17000
  }
}
watch(() => folder, (folder) => {
  let v = folder.value
  cy.json({elements: v})
  onChangeVisualisationMode(selected_viz_type.value)
  makePopper(cy)
}, { deep: true })

function select_viz_relationships(selected_ids) {
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

function onChangeVisualisationMode(layout_name) {
  cy.layout(layoutConfig(layout_name)).run()
}

onMounted(() => {
  cy = cytoscape({
    container: document.getElementById('cy'),
    boxSelectionEnabled: false,
    elements: folder.value,
    ready: function() {
      let layoutUtilities = this.layoutUtilities({
        desiredAspectRatio: 2,
        fullness: 50,
        componentSpacing: 100
      });
      makeEvents(this)
    },
    layout: layoutConfig(selected_viz_type.value, false),
    style: style,
    elements: folder.value
  })
})

</script>

<style>
      body {
        overflow: hidden;
      }
      #cy {
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        right: 0;
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

</style>
