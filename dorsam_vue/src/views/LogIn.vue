<template>
    <div class="columns">
         <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="">Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>

                    <div class="field">
                        <label for="">Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors"> {{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log In</button>
                        </div>
                    </div>

                    <hr>
                   
                    Or <router-link to="/signUp"> Register </router-link> 
                </form>
         </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/v1/token/login/", formData)
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    
                    axios.defaults.headers.common["Authorization"] = "Token " + token
                    localStorage.setItem("token", token)
                    const toPath = this.$route.query.to || '/cart'
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }


    },
    mounted() {
        document.title = 'Log In | Dawesome'
    }
}
</script>