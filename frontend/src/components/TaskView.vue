<template>
  <div>
    <v-toolbar
      color="#424242"
      dark
      height="45"
    >
      <v-toolbar-title>作番リスト（受注済、作業中）</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card>
      <v-card-text>
    <v-data-table
            :headers="headers"
            :items="data"
            hide-actions
            class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td >{{ props.item.workno }}</td>
        <td >{{ props.item.title }}</td>
        <td >{{ props.item.customer }}</td>
        <td class="text-xs-right" >&yen;{{ props.item.price }}</td>
        <td >{{ props.item.start_data }}</td>
        <td >{{ props.item.end_date }}</td>
        <td >{{ props.item.user }}</td>
        <td class="text-xs-right" >{{ props.item.plan_day }}</td>
        <td class="text-xs-right" >{{ props.item.result_day }}</td>
        <td class="text-xs-right" :style="{backgroundColor: (parseFloat(props.item.aa) > 100 ? '#F06292' : 'transparent' ) }">{{ props.item.aa }}</td>
        <td class="text-xs-right" :style="{backgroundColor: (parseFloat(props.item.bb) > 100 ? '#F06292' : 'transparent' ) }">{{ props.item.bb }}</td>
        <td class="text-xs-right" :style="{backgroundColor: (parseFloat(props.item.cc) < 0 ? '#F06292' : 'transparent' ) }">{{ props.item.cc }}</td>
        <td class="text-xs-right" :style="{backgroundColor: (parseFloat(props.item.dd) < 0 ? '#F06292' : 'transparent' ) }">&yen;{{ props.item.dd }}</td>
      </template>
    </v-data-table>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  name: "TaskView",
  data() {
    return {
      headers: [
        { text: "作番", value: "workno" },
        { text: "案件名", value: "title" },
        { text: "顧客名", value: "customer" },
        { text: "受注金額", value: "price" },
        { text: "開始日", value: "start_data" },
        { text: "終了日", value: "end_date" },
        { text: "担当", value: "user" },
        { text: "計画（人日）", value: "plan_day" },
        { text: "実績（人日）", value: "result_day" },
        { text: "予算消化率", value: "aa" },
        { text: "日程経過率", value: "bb" },
        { text: "残工数（人日）", value: "cc" },
        { text: "残予算", value: "dd" }
      ],
      data: [
        {
          workno: "1807346",
          title: "生産管理ソリューション",
          customer: "A社",
          price: "5,500,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "田中",
          plan_day: 560.0,
          result_day: 390.0,
          aa: "78.9%",
          bb: "123%",
          cc: "180.0",
          dd: "1,298,900"
        },
        {
          workno: "1807346",
          title: "宛先不正メール確認簡易化作業",
          customer: "B社",
          price: "725,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "桜井",
          plan_day: 46.0,
          result_day: 11.0,
          aa: "23.5%",
          bb: "97%",
          cc: "447.0",
          dd: "458,760"
        },
        {
          workno: "1807346",
          title: "ソフトウェア開発業務",
          customer: "C社",
          price: "3,500,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "斉藤",
          plan_day: 370.0,
          result_day: 34.0,
          aa: "9.5%",
          bb: "84%",
          cc: "447.0",
          dd: "3,245,000"
        },
        {
          workno: "1807346",
          title: "NASリプレース",
          customer: "D社",
          price: "120,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "末永",
          plan_day: 18.0,
          result_day: 4.0,
          aa: "6.5%",
          bb: "71%",
          cc: "447.0",
          dd: "87,900"
        },
        {
          workno: "1807346",
          title: "生産管理ソリューション",
          customer: "E社",
          price: "4,500,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "田中",
          plan_day: 490.0,
          result_day: 520.0,
          aa: "123.5%",
          bb: "69%",
          cc: "447.0",
          dd: "-839,000"
        },
        {
          workno: "1807346",
          title: "生産管理システム移行前調査",
          customer: "F社",
          price: "1,500,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "岩崎",
          plan_day: 280.0,
          result_day: 290.0,
          aa: "103.5%",
          bb: "55%",
          cc: "447.0",
          dd: "-140,000"
        },
        {
          workno: "1807346",
          title: "ネズミ駆除WEBサイト構築",
          customer: "G社",
          price: "1,300,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "溝川",
          plan_day: 69.0,
          result_day: 23.0,
          aa: "44.5%",
          bb: "42%",
          cc: "447.0",
          dd: "340,000"
        },
        {
          workno: "1807346",
          title: "X線検査機ソフト開発",
          customer: "H社",
          price: "5,500,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "下津",
          plan_day: 560.0,
          result_day: 123.0,
          aa: "20.5%",
          bb: "22%",
          cc: "447.0",
          dd: "2,340,000"
        },
        {
          workno: "1807346",
          title: "生産管理ソリューション",
          customer: "I社",
          price: "3,500,000",
          start_data: "2018/11/05",
          end_date: "2019/03/06",
          user: "田中",
          plan_day: 560.0,
          result_day: 123.0,
          aa: "23.5%",
          bb: "12%",
          cc: "447.0",
          dd: "3,140,000"
        }
      ]
    };
  },
  methods: {
    fetchData() {
      let searchKey =
        "?name=" +
        this.filter_name +
        "&created_at_from=" +
        this.filter_created_at_from +
        "&created_at_to=" +
        this.filter_created_at_to;
      axios.get("/api/customers/" + searchKey).then(res => {
        this.data = res.data.results;
      });
    }
  },
  mounted() {
    //this.fetchData()
  },
  filters: {
    printDate(val) {
      return moment(val)
        .locale("ja")
        .format("YYYY/MM/DD");
    }
  }
};
</script>