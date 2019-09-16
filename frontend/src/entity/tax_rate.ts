/**
 * 税タイプ
 */
export enum TAX_TYPES {
    // 内税
    INCLUDE = 1,
    // 外税
    EXCLUDE = 2
};

/**
 * 税区分
 */
export enum TAX_OPTIONS {
    // 通常
    NORMAL = 1,
    // 軽減税率
    REDUCED = 2
};

/**
 * 税率モデル
 */
export interface TaxRate {
    rate: number;
    reduced_rate: number;
    start_date: Date;
    tax_type: TAX_TYPES;
};
