<template>
  <div>
        <v-toolbar
      color="#424242"
      dark
      height="42"
    >
      <v-toolbar-title>分類別作業時間</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card>
      <v-card-text>
    <pie-chart :data="[['日通請負', 33], ['日立請負', 28], ['AE請負', 22], ['中小支援', 13], ['受託開発', 24]]"></pie-chart>
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
