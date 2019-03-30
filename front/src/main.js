// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import MintUI from 'mint-ui'
import {
  Navbar,
  TabItem,
  TabContainer,
  TabContainerItem,
  Search,
  Button,
  Lazyload,
  IndexList,
  IndexSection,
  Field
} from 'mint-ui';
import 'mint-ui/lib/style.css'
import router from './router'

Vue.config.productionTip = false

Vue.use(MintUI)
Vue.component(Navbar.name, Navbar);
Vue.component(TabItem.name, TabItem);
Vue.component(TabContainer.name, TabContainer);
Vue.component(TabContainerItem.name, TabContainerItem);
Vue.component(Search.name, Search);
Vue.component(Button.name, Button);
Vue.use(Lazyload);
Vue.component(IndexList.name, IndexList);
Vue.component(IndexSection.name, IndexSection);
Vue.component(Field.name, Field);


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
