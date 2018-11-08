<template>
    <div>
        <v-card>
            <v-toolbar color="#424242" dark dense card>
                <v-toolbar-title>作業表　2018年 11月</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-btn color="success" @click="save()">保存</v-btn>
                <v-btn color="error" @click="deleteData()">提出する</v-btn>
            </v-toolbar>
            <v-card-text>
                <work-records-hot-table :data="WorkRecords"></work-records-hot-table>
            </v-card-text>
        </v-card>
    </div>
</template>

<script>
import WorkRecordsHotTable from "../components/WorkRecordsHotTable.vue";

export default {
  name: "WorkRecords",
  components: {
    WorkRecordsHotTable
  },
  data() {
    return {
      WorkRecords: null,
      user: [{ dep: null }, { no: null }, { name: null }]
    };
  },
  methods: {},
  created() {}
};
</script>