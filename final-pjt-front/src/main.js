import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
// material design icons
import "@mdi/font/css/materialdesignicons.css";

const app = createApp(App);
const pinia = createPinia();
const vuetify = createVuetify({
  components,
  directives,
});

pinia.use(piniaPluginPersistedstate);
// app.use(createPinia())
app.use(pinia);
app.use(router);
app.use(vuetify);

app.mount("#app");
