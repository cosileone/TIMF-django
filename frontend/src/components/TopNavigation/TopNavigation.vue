<template>
    <el-menu class="navigation" mode="horizontal">
        <el-menu-item route="/">
            <div>
                <img class="navigation__logo" :src="require('@/assets/logo.png')" alt="Time is Money Friend Logo (Temporary)">
                <span>Time is Money, Friend</span>
            </div>
        </el-menu-item>
        <el-menu-item>
            <router-link class="navigation__link" to="/">Home</router-link>
        </el-menu-item>
        <el-menu-item>
            <router-link class="navigation__link" to="/about">Login</router-link>
        </el-menu-item>
        <el-menu-item>
            <router-link class="navigation__link" to="/register">
                <el-button>Sign Up</el-button>
            </router-link>
        </el-menu-item>
    </el-menu>
</template>

<script>
  export default {
    name: "TopNavigation"
  }
</script>

<style lang="scss">
    .navigation {
        padding: 8px;

        &__logo {
            height: 60px;
        }

        &__link {
            text-decoration: none;
        }
    }
</style>
