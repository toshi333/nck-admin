<template>
  <hot-table :root="root" :settings="hotSettings" ref="productGrid"></hot-table>
</template>

<script>
import HotTable from "vue-handsontable-official";

const productUnitChoice = ["個", "台", "式", "kg", "m"];

export default {
  name: "ProductHotTable",
  props: ["data"],
  components: {
    HotTable
  },
  data() {
    return {
      root: "testhot",
      hotSettings: {
        data: this.data,
        colHeaders: ["製品名", "単位", "単価", "税込単価"],
        columns: [
          { data: "name", type: "text" },
          { data: "unit", type: "dropdown", source: productUnitChoice },
          {
            data: "unit_price",
            type: "numeric",
            numericFormat: { pattern: "0,0" }
          },
          {
            data: "taxprice",
            type: "numeric",
            numericFormat: { pattern: "0,0.0" }
          }
        ],
        autoColumnSize: true,
        enterBeginsEditing: false,
        rowHeights: 30,
        minSpareRows: 1,
        minRows: 3,
        stretchH: "all",
        contextMenu: true,
        manualColumnResize: true,
        rowHeaders: true,
        afterChange: (changes, source) => {
          if (source === "edit") {
            this.calc();
          }
        }
      }
    };
  },
  methods: {
    calc() {
      this.data.forEach(row => {
        row.taxprice = !row.unit_price ? null : row.unit_price * 1.08;
      });
      this.$refs.productGrid.table.render()
    }
  },
  mounted() {
    this.calc();
  }
};
</script>