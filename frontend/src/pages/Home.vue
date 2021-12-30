<script setup>
import { ref } from 'vue';
import { deleteFolder, createFolder } from '../api';
import { useFolders } from '../hooks';
import { useRouter } from 'vue-router'

const router = useRouter()
const { folders, isLoading, refetch } = useFolders();


const confirm_delete_dialog = ref(false)
const create_folder_dialog = ref(false)

const new_folder_name = ref();
var remove_folder_name = null;

function click_delete_dialog(folder_name) {
  remove_folder_name = folder_name
  this.confirm_delete_dialog = true
}

function delete_dialog() {
  deleteFolder(remove_folder_name).then(r => {
    refetch.value()
  })
}

function add_new_folder() {
  if (new_folder_name.value && new_folder_name.value.length >= 3 ) {
    createFolder(new_folder_name.value).then(r => {
      refetch.value()
      this.create_folder_dialog = false
    })
  }
}
</script>

<template>
  <div class="q-pa-md q-gutter-md">

    <q-btn color="positive" text-color="dark" icon="add" label="Create a folder" @click="create_folder_dialog = true"/>

    <q-inner-loading
        :showing="isLoading"
        label="Loading folders..."
        label-class="text-primary"
        color="primary"
        label-style="font-size: 1.1em"
        size="5.5em"
    />

    <p v-if="folders && folders.length == 0">You dont have any folders yet !</p>
    <q-list style="rounded-borders; overflow-y: auto;" v-else>
      <q-item-label header>My folders</q-item-label>
      <p v-for="(folder, index) of folders" :key="folder.name" @click="router.push({path: `/v/${folder.identifier}`})">
        <q-item v-ripple  >
          <q-item-section avatar top>
            <q-avatar icon="folder" color="primary" text-color="black" size="30px;"/>
          </q-item-section>

          <q-item-section top class="col-2 gt-sm">
            <q-item-label class="q-mt-sm">{{ folder.name }}</q-item-label>
          </q-item-section>

          <q-item-section top>
            <q-item-label lines="1">
              <span>Created at: </span>
              <span class="text-weight-medium"> {{ folder.timestamp }}</span>
            </q-item-label>
            <q-item-label caption lines="1"> {{ folder.summary }}</q-item-label>
          </q-item-section>

          <q-item-section side>
            <div class="text-grey-8 q-gutter-xs">
              <q-btn color="negative" icon="delete" v-on:click.stop="click_delete_dialog(folder.identifier)"/>
            </div>
          </q-item-section>
        </q-item>

        <q-separator spaced v-if="index != folders.length - 1"/>
      </p>
    </q-list>

    <q-dialog v-model="confirm_delete_dialog">
      <q-card>
        <q-card-section class="row items-center">
          <q-avatar icon="warning" color="red" text-color="white" />
          <span class="q-ml-sm">Are you sure you want to delete the folder?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="No" color="primary" v-close-popup />
          <q-btn flat label="Yes" color="primary" v-close-popup @click="delete_dialog()"/>
        </q-card-actions>
      </q-card>
    </q-dialog>

    <q-dialog v-model="create_folder_dialog">

      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Name of the new folder</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input 
            dense 
            v-model="new_folder_name"
            autofocus
            :rules="[
                val => !!val || 'Please set a folder name',
                val => val.length >= 3 || 'The name of the folder must contain at least 3 characters',
              ]"
            @keyup.enter="prompt = false" 
          />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn flat label="Add address" @click="add_new_folder()"/>
        </q-card-actions>
      </q-card>

    </q-dialog>

  </div>
</template>

<style>
</style>
