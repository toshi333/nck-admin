import Vue from 'vue'
import Router from 'vue-router'
import DashBoard from './views/DashBoard.vue'
import UserProfile from './views/UserProfile.vue'
import WorkRecords from './views/WorkRecords.vue'
import CustomerIndex from './views/CustomerIndex.vue'
import CustomerDetail from './views/CustomerDetail.vue'

Vue.use(Router)

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'DashBoard',
      component: DashBoard
    },
    {
      path: '/user_profile/:id',
      name: 'UserProfile',
      component: UserProfile
    },
    {
      path: '/work_records',
      name: 'WorkRecords',
      component: WorkRecords
    },
    {
      path: '/customer_index',
      name: 'CustomerIndex',
      component: CustomerIndex
    },
    {
      path: '/customer_detail/:id',
      name: 'CustomerDetail',
      component: CustomerDetail
    },
  ]
})
