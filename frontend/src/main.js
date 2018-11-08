import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import VueChartkick from 'vue-chartkick'
import Chart from 'chart.js'
import Sortable from 'vue-sortable'

Vue.use(Sortable)
Vue.use(VueChartkick, {adapter: Chart})
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
