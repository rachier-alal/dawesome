<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6" >Welcome to dorsam</p>
        <p class="subtitle">Best baby store online</p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <div class="column is-3" v-for="product in latestProducts" :key="product.id">
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
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  data(){
    return{
      latestProducts: []
    }
  },
  components: {
    
  },
  mounted(){
    this.getLatestProducts()

    document.title =  'Shop | Dawasome'
  },
  methods: {
    async getLatestProducts(){
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest_products')
        .then(response =>{
          this.latestProducts = response.data
          
        })
        .catch(error => {
          console.log(error)
        })

         this.$store.commit('setIsLoading', false)

    }
  }
}
</script>

<style>
  .image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
