<template>
  <v-layout row wrap>
    <v-flex ma-1 xs-5 v-sortable>
      <working-rate></working-rate>
    </v-flex>
    <v-flex ma-1 xs-3>
      <overtime></overtime>
    </v-flex>
    <v-flex ma-1 xs-3>
      <overtime-total></overtime-total>
    </v-flex>
    <v-flex ma-1 xs-12>
      <task-view></task-view>
    </v-flex>
    <v-flex ma-1 xs-6>
      <chart></chart>
    </v-flex>
    <v-flex ma-1 xs-4>
      <chart2></chart2>
    </v-flex>
  </v-layout>
</template>

<script>
import TaskView from "../components/TaskView.vue";
import Chart from "../components/Chart.vue";
import Chart2 from "../components/Chart2.vue";
import Overtime from "../components/Overtime.vue";
import OvertimeTotal from "../components/OvertimeTotal.vue";
import WorkingRate from "../components/WorkingRate.vue";

export default {
  name: "DashBoard",
  components: {
    TaskView,
    Chart,
    Chart2,
    Overtime,
    OvertimeTotal,
    WorkingRate
  },
  data() {
    return {};
  },
  methods: {}
};
</script>