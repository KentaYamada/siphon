import Vue from 'vue';
import _ from 'lodash';
import CategoryService from '@/api/category.service';
import { Item } from '@/entity/item';
import ItemService from '@/api/item.service';
import { AxiosResponse } from 'axios';


export default Vue.extend({
    props: {
        item: {
            required: true
        }
    },
    data() {
        return {
            categories: [],
            errors: {}
        };
    },
    mounted() {
        CategoryService.fetchCategories()
            .then((response: AxiosResponse<any>) => {
                this.categories = response.data.categories;
            })
            .catch((error: any) => {
                console.error(error);
            });
    },
    methods: {
        /**
         * 保存イベント
         */
        handleSave(): void { 
            ItemService.saveItem(this.item as Item)
                .then((response: AxiosResponse<any>) => {
                    this.$emit('close');
                    this.$emit('save-success', response.data.message);
                })
                .catch((error: any) => {
                    const response = error.response;

                    if (!_.isEmpty(response.data.errors)) {
                        this.errors = _.extend({}, response.data.errors);
                    }
                    const message = `<p>${response.data.message}</p>`;
                    this.$toast.open({
                        message: message,
                        type: 'is-danger'
                    });
                });
        }
    }
});
