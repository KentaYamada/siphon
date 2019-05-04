import moment from 'moment';

/**
 * メニューモデル
 */
export interface Menu {
    title: string;
    icon: string;
    url?: string;
    submenu: Menu[] | null;
}

/**
 * メニュー取得
 */
export function getMenus(): Menu[] {
    const today = moment().format('YYYY-MM-DD');
    const dailySalesUrl = `/sales/daily?sales_date=${today}`;

    // 売上メニュー
    const salesMenu: Menu = {
        title: '売上',
        icon: 'fa-coins',
        submenu: [
            {title: '売上登録', icon: 'fa-cash-register', url: '/cashier', submenu: null},
            {title: '1日の売上', icon: 'fa-calendar-day', url: dailySalesUrl, submenu: null}
        ]
    };

    // マスタメニュー
    const settingMenu: Menu = {
        title: '設定',
        icon: 'fa-user-cog',
        submenu: [
            {title: '商品カテゴリ', icon: 'fa-tag', url: '/categories', submenu: null},
            {title: '商品', icon: 'fa-coffee', url: '/items', submenu: null},
            {title: 'ユーザー', icon: 'fa-users', url: '/users', submenu: null}
        ]
    };

    return [salesMenu, settingMenu];
}