<template>
  <div>
        <v-toolbar
      color="#424242"
      dark
      height="42"
    >
      <v-toolbar-title>月別 売上予実績</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card>
      <v-card-text>
    <column-chart :data="chartData" :colors="['#4169E1', '#FE2E64']" :dataset="{borderWidth: 1}"></column-chart>
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
          name: "予算",
          data: {
            "4月": 1400,
            "5月": 1700,
            "6月": 1500,
            "7月": 1890,
            "8月": 1940,
            "9月": 1780,
            "10月": 1560,
            "11月": 1770,
            "12月": 1900,
            "1月": 1400,
            "2月": 1320,
            "3月": 1420
          }
        },
        {
          name: "実績",
          data: {
            "4月": 1930,
            "5月": 1630,
            "6月": 1770,
            "7月": 1510,
            "8月": 1820,
            "9月": 1910,
            "10月": 1810,
            "11月": 1100,
            "12月": 0,
            "1月": 0,
            "2月": 0,
            "3月": 0
          }
        }
      ]
    };
  }
};
</script>
