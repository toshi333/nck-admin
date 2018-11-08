<template>
  <v-card>
    <v-toolbar color="#424242" dark dense card>
      <v-toolbar-title>顧客一覧</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-layout row wrap>
        <v-flex ma-1 xs-3>
          <v-text-field label="名前" v-model="filter_name"></v-text-field>
        </v-flex>
        <v-flex ma-1 xs-3>
          <DatePicField label="登録日From" v-model="filter_created_at_from"></DatePicField>
        </v-flex>
        <v-flex ma-1 xs-3>
          <DatePicField label="登録日To" v-model="filter_created_at_to"></DatePicField>
        </v-flex>
        <v-flex ma-1 xs-3>
          <v-btn color="info" @click="fetchData()">検索</v-btn>
        </v-flex>
      </v-layout>
      <v-spacer></v-spacer>
      <v-btn color="info" @click="$router.push('/customer_detail/0')">新規作成</v-btn>
      <v-data-table :headers="headers" :items="data" hide-actions class="elevation-1">
        <template slot="items" slot-scope="props">
          <td>{{ props.item.id }}</td>
          <td>
            <router-link :to="{ name: 'CustomerDetail', params: {id: props.item.id}}">{{ props.item.name }}</router-link>
          </td>
          <td>{{ props.item.rank }}</td>
          <td>{{ props.item.user }}</td>
          <td>{{ props.item.created_at|printDate }}</td>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
import moment from "moment";
import api from "../util/api";
import DatePicField from "../components/DatePicField.vue";

export default {
  name: "CustomerIndex",
  components: {
    DatePicField
  },
  data() {
    return {
      filter_name: "",
      filter_created_at_from: "",
      filter_created_at_to: "",
      headers: [
        { text: "ID", value: "id" },
        { text: "顧客名", value: "name" },
        { text: "ランク", value: "rank" },
        { text: "担当者", value: "user" },
        { text: "登録日時", value: "created_at" }
      ],
      data: []
    };
  },
  methods: {
    fetchData() {
      // 検索条件文字列
      let searchKey =
        "?name=" +
        this.filter_name +
        "&created_at_from=" +
        this.filter_created_at_from +
        "&created_at_to=" +
        this.filter_created_at_to;
      // 一覧取得API
      api.list("/api/masters/customers/", searchKey).then(res => {
        this.data = res.results;
      });
    }
  },
  created() {
    this.fetchData();
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