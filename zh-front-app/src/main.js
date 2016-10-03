import Vue from 'vue';
import App from './app/home/modules';
import router from './router';

router.star(App, 'body');
/* eslint-disable no-new */
// new Vue({
//   el: 'body',
//   components: { App }
// })
