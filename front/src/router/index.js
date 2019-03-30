import Vue from 'vue'
import Router from 'vue-router'
import Schedule from '@/components/Schedule'
import SearchPrepod from '@/components/SearchPrepod'
import SearchPrepodByPhoto from '@/components/SearchPrepodByPhoto';
import Prepod from '@/components/Prepod';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SearchPrepod',
      component: SearchPrepod
    },
    {
      path: '/schedule',
      name: 'Schedule',
      component: Schedule
    },
    {
      path: '/search',
      name: 'SearchPrepodByPhoto',
      component: SearchPrepodByPhoto
    },
    {
      path: '/prepod/:id',
      name: 'Prepod',
      component: Prepod
    },
  ]
})
