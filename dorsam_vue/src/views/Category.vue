<template>
<div class="page-category">
    <div class="columns is-multiline">
        <div class="columns is-12">
            <div class="is-size-2 has-text-centered">
                <h2>{{ category.name}}</h2>
            </div>
        </div>
        <div class="column is-3" v-for="product in category.products" :key="product.id">
                <div class="box">
                <figure class="image mb-4">
                    <img :src="product.get_thumbnail" alt="no image to display">
                </figure>
                <h3 class="is-size-4">{{ product.name }}</h3>
                <p class="is-size-6 has-text-grey">${{ product.price }}</p>
                <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
                </div>
            </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Category',
    data(){
        return{
            category: {
                products: []
            }
        }
    },
    mounted() {
         this.getCategory()
    },
    methods: {
        async getCategory() {
            const category_slug = this.$route.params.category_slug
             this.$store.commit('setIsLoading', true)

             axios
                .get(`/api/v1/products/${category_slug}/`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name + ' | Dawasome'
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something went wrong, try again.',
                        type: 'is-warning',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-center'
                    })
                })
             this.$store.commit('setIsLoading', false)

        }
    }
}
</script>