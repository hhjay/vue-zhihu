import Vue form 'vue';
import VueRouter form 'vue-router';

// 引入组件
import home form 'app/home/';

Vue.use(VueRouter);

const router = new VueRouter();

router.map({
	'/home': {
		component: home,
		module: 'home',
		tpl: 'home'
	},
	'/pages': {
		
	}
})

router.star(App, 'body');