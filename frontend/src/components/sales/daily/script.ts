import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import DailySalesItem from '@/components/sales/daily/item/DailySalesItem.vue';
import { DailySalesSearchOption } from '@/entity/daily_sales';

const getDummy = () => {
    let list = [];

    for (let i = 1; i < 10; i++) {
        list.push({
            sales_id: i,
            total_price: 1000,
            sales_date: '2019年04月04日 09:32:29',
            discount: 0,
            sales_items: [
                {
                    id: 1,
                    item_name: 'Item A',
                    unit_price: 300,
                    quantity: 1
                },
                {
                    id: 2,
                    item_name: 'Item B',
                    unit_price: 400,
                    quantity: 2
                },
                {
                    id: 3,
                    item_name: 'Item C',
                    unit_price: 500,
                    quantity: 3
                }
            ]
        });
    }

    return list;
};

/**
 * 日次売上一覧
 */
export default Vue.extend({
    data() {
        const option: DailySalesSearchOption = {
            sales_date: null,
            time_from: '',
            time_to: '',
            q: ''
        };

        return {
            option,
            dailySales: getDummy()
        };
    },
    mounted() {
        //this.fetchDailySales(this.option);
    },
    components: {
        DailySalesItem
    },
    computed: {
        ...mapGetters('daily_sales', [
            'getDailySales',
            'hasItems'
        ]),
        title(): string {
            const params = this.$route.params;
            return `${params.year}年${params.month}月${params.day}の売上`; 
        },
    },
    methods: {
        ...mapActions('daily_sales', [
            'fetchDailySales'
        ]),
        /**
         * 売上検索
         */
        handleSearch(): void {
            // this.fetchDailySales(this.option);
        },
        /**
         * 検索条件クリア
         */
        handleClearConditions(): void {
            this.option.sales_date = null;
            this.option.time_from = '';
            this.option.time_to = '';
            this.option.q = '';
        }
    }
});
