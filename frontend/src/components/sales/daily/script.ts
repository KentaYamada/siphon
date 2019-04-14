import Vue from 'vue';
import {
    mapActions,
    mapGetters
} from 'vuex';
import moment from 'moment';
import _ from 'lodash';
import DailySalesItem from '@/components/sales/daily/item/DailySalesItem.vue';
import { DailySalesSearchOption } from '@/entity/daily_sales';


const getDummy = () => {
    let list = [];

    for (let i = 1; i < 10; i++) {
        let is_equal = i % 2 === 0;
        list.push({
            sales_id: i,
            total_price: is_equal ? -1000 : 1000,
            grand_total_price: is_equal ? -1000 : 1000,
            sales_date: moment().format('YYYY年MM月DD日 HH:mm:ss'),
            discount: 0,
            is_cancel: is_equal,
            sales_items: [
                {
                    id: 1,
                    item_name: 'Item A',
                    unit_price: 300,
                    quantity: is_equal ? -1 : 1
                },
                {
                    id: 2,
                    item_name: 'Item B',
                    unit_price: 400,
                    quantity: is_equal ? -2 : 2
                },
                {
                    id: 3,
                    item_name: 'Item C',
                    unit_price: 500,
                    quantity: is_equal ? -3 : 3
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

        const params = this.$route.params;

        if (_.isUndefined(params) || _.isNull(params)) {
            option.sales_date = moment().toDate();
        } else {
            const year: number = +params.year;
            const month: number = +params.month;
            const day: number = +params.day;
            option.sales_date = new Date(year, month, day);
        }

        return {
            option,
            dailySales: getDummy()
        };
    },
    mounted() {
        this.fetchDailySales(this.option);
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
            return `${moment().format('YYYY年MM月DD日')}の売上`;
            //const params = this.$route.params;
            //return `${params.year}年${params.month}月${params.day}の売上`; 
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
