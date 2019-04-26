import Vue from 'vue'
import { Button, Menu, MenuItem } from 'element-ui'
import lang from 'element-ui/lib/locale/lang/en'
import locale from 'element-ui/lib/locale'

locale.use(lang);

Vue.use(Button);
Vue.use(Menu);
Vue.use(MenuItem);
