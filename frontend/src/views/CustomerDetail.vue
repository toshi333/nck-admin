<template>
  <v-card v-if="customerData">
    <v-toolbar color="#424242" dark dense card>
      <v-btn icon class="hidden-xs-only" @click="$router.push('/customer_index')">
        <v-icon>arrow_back</v-icon>
      </v-btn>
      <v-toolbar-title>顧客情報</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="success" :loading="loading" :disabled="loading" @click="save()">保存</v-btn>
      <v-btn color="info" @click="copy()">コピー</v-btn>
      <v-btn color="error" @click="deleteDialog = true">削除</v-btn>
    </v-toolbar>
    <v-card-text>
      <v-alert :value="alert" type="error" dismissible>
        {{alert}}
      </v-alert>
      <v-form>
        <v-layout row wrap>
          <v-flex ma-1 xs-3>
            <v-text-field v-model="customerData.id" label="ID" required readonly></v-text-field>
          </v-flex>
          <v-flex ma-1 xs-3>
            <v-text-field v-model="customerData.name" label="名前" required></v-text-field>
          </v-flex>
          <v-flex ma-1 xs-3>
            <v-select v-model="customerData.rank" :items="rankSelectItems" item-text="text" item-value="rank" label="ランク" return-masked-value></v-select>
          </v-flex>
          <v-flex ma-1 xs-3>
            <v-autocomplete v-model="customerData.user" :items="userSelectItems" item-text="name" item-value="id" label="担当者" return-masked-value></v-autocomplete>
          </v-flex>
          <v-flex ma-1 xs-3>
            <v-text-field v-model="customerData.created_at" label="登録日時" required></v-text-field>
          </v-flex>
        </v-layout>
      </v-form>

      <div class="subheading">製品</div>
      <product-hot-table :data="customerData.product"></product-hot-table>
    </v-card-text>
    <v-dialog v-model="deleteDialog" max-width="500">
      <v-card>
        <v-card-title class="headline grey lighten-1" dense>確認</v-card-title>
        <v-card-text>
          <span>このデータを削除しますか？</span>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" @click="deleteData()">削除</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-snackbar v-model="saveOk" color="success" :timeout=2500>
      <span class="text-center">保存しました。</span>
    </v-snackbar>
    <v-snackbar v-model="copyOk" color="info" :timeout=2500>
      <span class="text-lg-center">コピーしました。</span>
    </v-snackbar>
  </v-card>

</template>

<script>
import ProductHotTable from "../components/ProductHotTable.vue";
import DatePicField from "../components/DatePicField.vue";
import api from "../util/api.js";

const rankChoice = [
  { rank: "A", text: "A:優先" },
  { rank: "B", text: "B:通常" },
  { rank: "C", text: "C:維持" }
];
const userChoice = [
  { id: 1, name: "田中俊行" },
  { id: 2, name: "山田孝之" },
  { id: 3, name: "ムロツヨシ" }
];

export default {
  name: "CustomerDetail",
  components: {
    ProductHotTable,
    DatePicField
  },
  data() {
    return {
      rankSelectItems: rankChoice,
      userSelectItems: userChoice,
      customerData: null,
      saveOk: false,
      copyOk: false,
      loading: false,
      alert: null,
      deleteDialog: false
    };
  },
  methods: {
    // 更新処理の前にグリッドの空白行を除去する
    deleteEmptyRow(data) {
      return data.filter(row => {
        let isNul = false;
        for (let col in row) {
          if (row[col] !== null) isNul = true;
        }
        return isNul;
      });
    },

    // 登録/更新処理
    save() {
      this.loading = true;
      this.customerData.product = this.deleteEmptyRow(
        this.customerData.product
      );
      api
        .save("/api/masters/customers/", this.customerData)
        .then(() => {
          this.saveOk = true;
        })
        .catch(error => {
          this.alert = error.response.data;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    deleteData() {
      this.loading = true;
      api
        .delete("/api/masters/customers/", this.customerData.id)
        .then(() => {
          this.$router.push("/customer_index");
        })
        .catch(error => {
          this.alert = error.response.data;
        });
    },
    // コピーボタンを押すと、主キーをクリアする
    copy() {
      this.customerData.id = 0;
      this.customerData.product.forEach(element => {
        element.id = null
        element.customer = null;
      });
      this.copyOk = true;
    }
  },
  created() {
    if (this.$route.params.id != 0) {
      // 一覧取得API
      api
        .list("/api/masters/customers/", this.$route.params.id)
        .then(res => {
          this.customerData = res;
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      this.customerData = {
        id: null,
        name: null,
        rank: null,
        user: null,
        product: []
      };
    }
  }
};
</script>