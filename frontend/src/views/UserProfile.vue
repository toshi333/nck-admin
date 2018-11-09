<template>
  <v-card>
    <v-toolbar color="#424242" dark dense card>
      <v-toolbar-title>プロフィール</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="success" :loading="loading" :disabled="loading" @click="save()">保存</v-btn>
    </v-toolbar>
    <v-card-text>
      <v-alert :value="alert" type="error" dismissible>
        {{alert}}
      </v-alert>
      <v-form ref="form">

        <v-text-field name="username" v-model="data.username" label="ユーザー名" required></v-text-field>
        <v-text-field name="last_name" v-model="data.last_name" label="性"></v-text-field>
        <v-text-field name="first_name" v-model="data.first_name" label="名"></v-text-field>
        <v-text-field name="email" v-model="data.email" label="メール" required></v-text-field>

        <v-text-field label="プロフィール画像" @click='pickFile' v-model='imageName' prepend-icon='attach_file'></v-text-field>
        <input type="file" name="profile_picture" style="display: none" ref="image" accept="image/*" @change="onFilePicked">
        <img :src="imageUrl" height="150" v-if="imageUrl" />

      </v-form>
    </v-card-text>
    <v-snackbar v-model="saveOk" color="success" :timeout=2500>
      <span class="text-center">保存しました。</span>
    </v-snackbar>
  </v-card>

</template>

<script>
import api from "../util/api.js";

export default {
  name: "UserProfile",
  components: {},
  data() {
    return {
      data: [],
      saveOk: false,
      loading: false,
      alert: null,

      dialog: false,
      imageName: "",
      imageUrl: "",
      imageFile: ""
    };
  },
  methods: {
    // 登録/更新処理
    save() {
      this.loading = true;
      let formData = new FormData();
      formData.append("id", this.data.id)
      formData.append("username", this.data.username)
      formData.append("last_name", this.data.last_name)
      formData.append("first_name", this.data.first_name)
      formData.append("email", this.data.email)
      formData.append("profile_picture", this.data.profile_picture)
      // このようにFormDataを一から作り値を詰め込む必要はないはずだが。。。スマートな方法求む
      
      api
        .update("/api/masters/users/", this.data.id, formData, "multipart/form-data")
        .then(() => {
          this.saveOk = true;
        })
        .catch(error => {
          this.alert = error;
        })
        .finally(() => {
          this.loading = false;
        });
    },

    pickFile() {
      this.$refs.image.click();
    },

    onFilePicked(e) {
      const files = e.target.files;
      if (files[0] !== undefined) {
        this.imageName = files[0].name;
        if (this.imageName.lastIndexOf(".") <= 0) {
          return;
        }
        const fr = new FileReader();
        fr.readAsDataURL(files[0]);
        fr.addEventListener("load", () => {
          this.imageUrl = fr.result;
          this.data.profile_picture = files[0];
        });
      } else {
        this.imageName = "";
        this.imageFile = "";
        this.imageUrl = "";
      }
    }
  },
  created() {
    // 一覧取得API
    api
      .list("/api/masters/users/", this.$route.params.id)
      .then(res => {
        this.data = res;
      })
      .catch(error => {
        this.alert = error.response.data;
      });
  }
};
</script>