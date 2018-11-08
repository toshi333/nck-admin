<template>
  <div>
        <v-toolbar
      color="#424242"
      height="42"
      dark
    >
      <v-toolbar-title>月別産業時間</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card>
      <v-card-text>
    <bar-chart :data="[['10月', 120], ['11月', 90], ['12月', 22],]"></bar-chart>
          </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Chart2",
  data() {
    return {
    };
  }
};
</script>
