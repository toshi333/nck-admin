<template>
  <div>
    <v-toolbar
    color="#424242"
    dark
    height="42"
    >
    <v-toolbar-title>月間残業（11月）</v-toolbar-title>
    <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>  
  <v-card>
    <v-card-text>
      <v-layout row wrap>
        <v-flex ma-1 xs-3>
          <p class="display-3 pink--text">12h / 32h</p>
        </v-flex>
        <v-flex ma-1 xs-3>
          <v-progress-circular
          :rotate="180"
          :size="100"
          :width="15"
          :value="value"
          color="pink"
          >
          {{ value }}%
          </v-progress-circular>
        </v-flex>
      </v-layout>
    </v-card-text>
  </v-card>
  </div>
</template>

<script>
export default {
  name: "Overtime",
  data() {
    return {
      value: 35
    };
  }
};
</script>
