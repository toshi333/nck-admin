<template>
  <v-app>
    <v-navigation-drawer fixed clipped app v-model="navBar" width="220" dark>
      <v-list dense>

        <v-list-tile @click="$router.push('/')" ripple>
          <v-list-tile-action>
            <v-icon>dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>ダッシュボード</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile @click="$router.push('/work_records')" ripple>
          <v-list-tile-action>
            <v-icon>event_note</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>作業表</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile>
          <v-list-tile-action>
            <v-icon>event_available</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>勤休表</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile>
          <v-list-tile-action>
            <v-icon>directions_subway</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>旅費申請</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile>
          <v-list-tile-action>
            <v-icon>assignment</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>発番申請</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile>
          <v-list-tile-action>
            <v-icon>assignment</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>見積申請</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile>
          <v-list-tile-action>
            <v-icon>assignment</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>購入申請</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile @click="$router.push('/customer_index')" ripple>
          <v-list-tile-action>
            <v-icon>person</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>顧客</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

      </v-list>
    </v-navigation-drawer>
    <v-toolbar dark color="#214c70" clipped-left fixed app>
      <v-toolbar-side-icon @click.stop="navBar = !navBar"></v-toolbar-side-icon>
      <v-toolbar-title class="white--text">NCK Admin</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>search</v-icon>
      </v-btn>

      <v-menu v-model="menu" :close-on-content-click="false" :nudge-width="200" offset-x left>
        <v-btn icon slot="activator">
          <v-icon>more_vert</v-icon>
        </v-btn>

        <v-card>
          <v-list>
            <v-list-tile avatar>
              <v-list-tile-avatar>
                <img :src="userInfo.userIcon">
              </v-list-tile-avatar>

              <v-list-tile-content>
                <v-list-tile-title>{{userInfo.userName}}</v-list-tile-title>
              </v-list-tile-content>

            </v-list-tile>

          <v-divider></v-divider>

            <v-divider></v-divider>
            <v-list-tile @click="userProfile()" ripple>
              <v-list-tile-action>
                <v-icon>event_note</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>プロフィール編集</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>

            <v-divider></v-divider>
            <v-list-tile href="/accounts/logout/" ripple>
              <v-list-tile-action>
                <v-icon>event_note</v-icon>
              </v-list-tile-action>
              <v-list-tile-content>
                <v-list-tile-title>ログアウト</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-menu>

    </v-toolbar>
    <v-content class="maincontent">
      <v-container fluid>
        <v-fade-transition mode="out-in">
          <router-view></router-view>
        </v-fade-transition>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      navBar: null,
      userInfo: userInfo,
      menu: false
    };
  },
  methods: {
    userProfile() {
      this.menu = false;
      this.$router.push('/user_profile/' + this.userInfo.userId)
    }
  },
  mounted: function() {},
  destroyed: function() {}
};
</script>

<style>
/* これを入れないとhandsontableのヘッダーがナビバーより上に表示される。もっといい方法あるかも */
.maincontent {
  z-index: 0;
}
</style>