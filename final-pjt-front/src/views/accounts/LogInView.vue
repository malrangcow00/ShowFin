<template>
  <!-- <div>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username" />
      </div>
      <div>
        <label for="password">password : </label>
        <input type="password" id="password" v-model.trim="password" />
      </div>
      <input type="submit" value="LOG IN" />
    </form>
  </div> -->

  <div>
    <v-img
      class="mx-auto my-6"
      max-width="400"
      src="../assets/img/login_logo.png"
    ></v-img>

    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">ID</div>

      <v-text-field
        v-model="username"
        density="compact"
        placeholder="ID를 입력해 주세요"
        :prepend-inner-icon="icon"
        variant="outlined"
        @click:prepend-inner="changeIcon"
      ></v-text-field>

      <div
        class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
      >
        Password

        <!-- <a
          class="text-caption text-decoration-none text-blue"
          href="#"
          rel="noopener noreferrer"
          target="_blank"
        >
          Forgot login password?</a
        > -->
      </div>

      <v-text-field
        v-model="password"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="비밀번호를 입력해 주세요"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>
      <!-- prettier-ignore -->
      <!-- <v-card class="mb-12" color="surface-variant" variant="tonal">
        <v-card-text class="text-medium-emphasis text-caption">
          금융 여정의 안심을 위한 출발, 지금 시작하세요. 가장 안전한 길로
          안내하는 금융 동반자. 금융의 바다를 함께 항해하는 동안, 안전하게
          목적지에 도달할 수 있도록 안내해 드립니다. 당신이 안심하고 여행을
          즐기실 수 있도록, 언제나 여러분 곁에 있습니다.
        </v-card-text>
      </v-card> -->

      <v-btn
        block
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        @click="logIn"
      >
        Log In
      </v-btn>

      <v-card-text class="text-center">
        <a
          class="text-blue text-decoration-none"
          @click.prevent="goSignUp"
          rel="noopener noreferrer"
          target="_blank"
        >
          Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
const router = useRouter();
const visible = ref(false);
const username = ref(null);
const password = ref(null);
const icons = ref([
  "mdi-emoticon",
  "mdi-emoticon-cool",
  "mdi-emoticon-dead",
  "mdi-emoticon-excited",
  "mdi-emoticon-happy",
  "mdi-emoticon-neutral",
  "mdi-emoticon-sad",
  "mdi-emoticon-tongue",
]);

const iconIndex = ref(0);
const icon = computed(() => icons.value[iconIndex.value]);

const changeIcon = () => {
  iconIndex.value =
    iconIndex.value === icons.value.length - 1 ? 0 : iconIndex.value + 1;
};

const logIn = function () {
  if (!username.value) {
    alert("아이디를 입력해주세요.");
    return;
  } else if (!password.value) {
    alert("비밀번호를 입력해주세요.");
    return;
  }
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};

const goSignUp = function () {
  router.push({ name: "SignUpView" });
};
</script>

<style scoped></style>
