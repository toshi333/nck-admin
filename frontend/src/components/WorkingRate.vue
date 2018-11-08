<template>
  <div>
        <v-toolbar
      color="#424242"
      dark
      height="42"
    >
      <v-toolbar-title>稼働率</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card>
      <v-card-text>
    <bar-chart :data="chartData" :colors="['#4169E1', '#FE2E64', '#009900']" :dataset="{borderWidth: 1}" :stacked="true" height="108px"></bar-chart>
          </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Chart",
  data() {
    return {
      chartData: [
        {
          name: "受注作番",
          data: {
            "IT活用BU": 2326.05,
          }
        },
        {
          name: "プレ作番",
          data: {
            "IT活用BU": 1405.75,
          }
        },
        {
          name: "社内作番",
          data: {
            "IT活用BU": 745.25,
          }
        },
        {
          name: "作番外",
          data: {
            "IT活用BU": 832.10,
          }
        },
      ]
    };
  }
};
</script>
