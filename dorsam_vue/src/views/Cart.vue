<template>
    <div class="page-cart">
        <div class="columms is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-full-width" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>

                    </thead>
                    <tbody>
                        <CartItem
                        v-for="item in cart.items"
                        v-bind:key="item.product.id"
                        v-bind:initialItem="item"
                        v-on:removeFromCart="removeFromCart"
                        />
                    </tbody>
                </table>
                <p v-else>You dont have any products in your cart ...</p>
            </div>
            <div class="column is-12 box">
                <div class="subtitle">Summary</div>
                <strong>Ksh. {{ cartTotalPrice.toFixed(2) }}, {{ cartTotalLength }} items </strong>
                <hr>
                <router-link to="/cart/checkout" class="button is-dark"> Proceed to checkout</router-link>
            </div> 
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    components: {
        CartItem
    },

    data() {
        return {
            cart: {
                items: []
            }
        }
    }, 
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        
        removeFromCart(item) {
            this.cart.items =  this.cart.items.filter(i => i.product.id !== item.product.id)   
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            },0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
    }
    
}
</script>