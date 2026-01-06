-- 코드를 입력하세요
SELECT 
    C.CAR_ID, 
    C.CAR_TYPE, 
    -- 30일간의 대여 금액 계산 (할인율 적용한 정수)
    FLOOR(C.DAILY_FEE * 30 * (1 - P.DISCOUNT_RATE / 100)) AS FEE
FROM 
    CAR_RENTAL_COMPANY_CAR AS C
JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P 
    ON C.CAR_TYPE = P.CAR_TYPE AND P.DURATION_TYPE = '30일 이상'
WHERE 
    C.CAR_TYPE IN ('세단', 'SUV') -- 1. 세단 또는 SUV만
    AND C.CAR_ID NOT IN (
        -- 2. 11월 한 달간 대여 기록이 있는 차 제외
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE END_DATE >= '2022-11-01' AND START_DATE <= '2022-11-30'
    )
-- 3. 계산된 금액이 50만 원 이상 200만 원 미만인 것만 필터링
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY 
    FEE DESC, 
    C.CAR_TYPE ASC, 
    C.CAR_ID DESC;

