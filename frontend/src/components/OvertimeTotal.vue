<template>
  <div>
        <v-toolbar
      color="#424242"
      dark
      height="42"
    >
      <v-toolbar-title>平均残業（2018下期）</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
  <v-card>
    <v-card-text>
      <v-layout row wrap>
        <v-flex ma-1 xs-3>
          <p class="display-3 teal--text">28h / 32h</p>
        </v-flex>
        <v-flex ma-1 xs-3>
          <v-progress-circular
          :rotate="180"
          :size="100"
          :width="15"
          :value="value"
          color="teal"
          >
          {{ value }}%
          </v-progress-circular>
        </v-flex>
      </v-layout>
    </v-card-text>
  </v-card>  </div>
</template>

<script>
export default {
  name: "Overtime",
  data() {
    return {
      value: 87
    };
  }
};
</script>
