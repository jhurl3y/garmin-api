from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class Root(BaseModel):
    message: str


class Name(BaseModel):
    name: str


class Step(BaseModel):
    startGMT: str
    endGMT: str
    steps: int
    primaryActivityLevel: str
    activityLevelConstant: bool


class Stats(BaseModel):
    userProfileId: int
    totalKilocalories: int
    activeKilocalories: int
    bmrKilocalories: int
    wellnessKilocalories: int
    burnedKilocalories: Optional[int] = None
    consumedKilocalories: Optional[int] = None
    remainingKilocalories: int
    totalSteps: int
    netCalorieGoal: Optional[int] = None
    totalDistanceMeters: int
    wellnessDistanceMeters: int
    wellnessActiveKilocalories: int
    netRemainingKilocalories: int
    userDailySummaryId: int
    calendarDate: str
    rule: dict
    uuid: str
    dailyStepGoal: int
    wellnessStartTimeGmt: Optional[datetime] = None
    wellnessStartTimeLocal: Optional[datetime] = None
    wellnessEndTimeGmt: Optional[datetime] = None
    wellnessEndTimeLocal: Optional[datetime] = None
    durationInMilliseconds: int
    wellnessDescription: Optional[str] = None
    highlyActiveSeconds: int
    activeSeconds: int
    sedentarySeconds: int
    sleepingSeconds: int
    includesWellnessData: bool
    includesActivityData: bool
    includesCalorieConsumedData: bool
    privacyProtected: bool
    floorsAscendedInMeters: float
    floorsDescendedInMeters: float
    floorsAscended: float
    floorsDescended: float
    intensityMinutesGoal: int
    userFloorsAscendedGoal: int
    minHeartRate: int
    maxHeartRate: int
    restingHeartRate: Optional[int] = None
    lastSevenDaysAvgRestingHeartRate: Optional[int] = None
    source: str
    averageStressLevel: int
    maxStressLevel: int
    stressDuration: int
    restStressDuration: int
    activityStressDuration: int
    uncategorizedStressDuration: int
    totalStressDuration: int
    lowStressDuration: int
    mediumStressDuration: int
    highStressDuration: int
    stressPercentage: float
    restStressPercentage: float
    activityStressPercentage: float
    uncategorizedStressPercentage: float
    lowStressPercentage: float
    mediumStressPercentage: float
    highStressPercentage: int
    stressQualifier: str
    measurableAwakeDuration: int
    measurableAsleepDuration: int
    lastSyncTimestampGMT: Optional[datetime] = None
    minAvgHeartRate: int
    maxAvgHeartRate: int
    bodyBatteryChargedValue: int
    bodyBatteryDrainedValue: int
    bodyBatteryHighestValue: int
    bodyBatteryLowestValue: int
    bodyBatteryMostRecentValue: int
    abnormalHeartRateAlertsCount: Optional[int] = None
    averageSpo2: Optional[int] = None
    lowestSpo2: Optional[int] = None
    latestSpo2: Optional[int] = None
    latestSpo2ReadingTimeGmt: Optional[datetime] = None
    latestSpo2ReadingTimeLocal: Optional[datetime] = None
    averageMonitoringEnvironmentAltitude: Optional[int] = None
    avgWakingRespirationValue: int
    highestRespirationValue: int
    lowestRespirationValue: int
    latestRespirationValue: int
    latestRespirationTimeGMT: str


class HeartRateDescriptor(BaseModel):
    key: str
    index: int


class HeartRate(BaseModel):
    userProfilePK: int
    calendarDate: str
    startTimestampGMT: datetime
    endTimestampGMT: datetime
    startTimestampLocal: datetime
    endTimestampLocal: datetime
    maxHeartRate: int
    minHeartRate: int
    restingHeartRate: int
    lastSevenDaysAvgRestingHeartRate: int
    heartRateValueDescriptors: List[HeartRateDescriptor]
    heartRateValues: List[List[Optional[int]]]


class Activity(BaseModel):
    activityId: int
    activityName: str
    description: Optional[str] = None
    startTimeLocal: datetime
    startTimeGMT: datetime
    activityType: dict
    eventType: dict
    comments: Optional[str] = None
    parentId: Optional[int] = None
    distance: float
    duration: float
    elapsedDuration: float
    movingDuration: float = None
    elevationGain: int
    elevationLoss: int
    averageSpeed: float
    maxSpeed: float
    startLatitude: float
    startLongitude: float
    hasPolyline: bool
    ownerId: int
    ownerDisplayName: str
    ownerFullName: str
    ownerProfileImageUrlSmall: str
    ownerProfileImageUrlMedium: str
    ownerProfileImageUrlLarge: str
    calories: int
    averageHR: int
    maxHR: int
    averageRunningCadenceInStepsPerMinute: float
    maxRunningCadenceInStepsPerMinute: int
    averageBikingCadenceInRevPerMinute: Optional[int] = None
    maxBikingCadenceInRevPerMinute: Optional[int] = None
    averageSwimCadenceInStrokesPerMinute: Optional[int] = None
    maxSwimCadenceInStrokesPerMinute: Optional[int] = None
    averageSwolf: Optional[int] = None
    activeLengths: Optional[int] = None
    steps: int
    conversationUuid: Optional[int] = None
    conversationPk: Optional[int] = None
    numberOfActivityLikes: Optional[int] = None
    numberOfActivityComments: Optional[int] = None
    likedByUser: Optional[int] = None
    commentedByUser: Optional[dict] = None
    activityLikeDisplayNames: Optional[list] = None
    activityLikeFullNames: Optional[list] = None
    requestorRelationship: Optional[str] = None
    userRoles: list
    privacy: dict
    userPro: bool
    courseId: Optional[int] = None
    poolLength: Optional[int] = None
    unitOfPoolLength: Optional[str] = None
    hasVideo: bool
    videoUrl: Optional[str] = None
    timeZoneId: int
    beginTimestamp: int
    sportTypeId: int
    avgPower: Optional[int] = None
    maxPower: Optional[int] = None
    aerobicTrainingEffect: Optional[int] = None
    anaerobicTrainingEffect: Optional[int] = None
    strokes: Optional[int] = None
    normPower: Optional[int] = None
    leftBalance: Optional[int] = None
    rightBalance: Optional[int] = None
    avgLeftBalance: Optional[int] = None
    max20MinPower: Optional[int] = None
    avgVerticalOscillation: Optional[int] = None
    avgGroundContactTime: Optional[int] = None
    avgStrideLength: float
    avgFractionalCadence: Optional[int] = None
    maxFractionalCadence: Optional[int] = None
    trainingStressScore: Optional[int] = None
    intensityFactor: Optional[int] = None
    vO2MaxValue: Optional[int] = None
    avgVerticalRatio: Optional[int] = None
    avgGroundContactBalance: Optional[int] = None
    lactateThresholdBpm: Optional[int] = None
    lactateThresholdSpeed: Optional[int] = None
    maxFtp: Optional[int] = None
    avgStrokeDistance: Optional[int] = None
    avgStrokeCadence: Optional[int] = None
    maxStrokeCadence: Optional[int] = None
    workoutId: Optional[int] = None
    avgStrokes: Optional[int] = None
    minStrokes: Optional[int] = None
    deviceId: int
    minTemperature: Optional[float] = None
    maxTemperature: Optional[float] = None
    minElevation: float
    maxElevation: int
    avgDoubleCadence: Optional[float] = None
    maxDoubleCadence: int
    summarizedExerciseSets: Optional[int] = None
    maxDepth: Optional[float] = None
    avgDepth: Optional[float] = None
    surfaceInterval: Optional[int] = None
    startN2: Optional[float] = None
    endN2: Optional[float] = None
    startCns: Optional[float] = None
    endCns: Optional[float] = None
    summarizedDiveInfo: dict
    activityLikeAuthors: Optional[dict] = None
    avgVerticalSpeed: Optional[float] = None
    maxVerticalSpeed: int
    floorsClimbed: Optional[int] = None
    floorsDescended: Optional[int] = None
    manufacturer: str
    diveNumber: Optional[int] = None
    locationName: str
    bottomTime: Optional[float] = None
    lapCount: int
    endLatitude: float
    endLongitude: float
    minAirSpeed: Optional[float] = None
    maxAirSpeed: Optional[float] = None
    avgAirSpeed: Optional[float] = None
    avgWindYawAngle: Optional[float] = None
    minCda: Optional[float] = None
    maxCda: Optional[float] = None
    avgCda: Optional[float] = None
    avgWattsPerCda: Optional[float] = None
    flow: Optional[float] = None
    grit: Optional[float] = None
    jumpCount: Optional[int] = None
    caloriesEstimated: Optional[int] = None
    caloriesConsumed: Optional[int] = None
    waterEstimated: Optional[int] = None
    waterConsumed: Optional[int] = None
    maxAvgPower_1: Optional[int] = None
    maxAvgPower_2: Optional[int] = None
    maxAvgPower_5: Optional[int] = None
    maxAvgPower_10: Optional[int] = None
    maxAvgPower_20: Optional[int] = None
    maxAvgPower_30: Optional[int] = None
    maxAvgPower_60: Optional[int] = None
    maxAvgPower_120: Optional[int] = None
    maxAvgPower_300: Optional[int] = None
    maxAvgPower_600: Optional[int] = None
    maxAvgPower_1200: Optional[int] = None
    maxAvgPower_1800: Optional[int] = None
    maxAvgPower_3600: Optional[int] = None
    maxAvgPower_7200: Optional[int] = None
    maxAvgPower_18000: Optional[int] = None
    excludeFromPowerCurveReports: Optional[bool] = None
    totalSets: Optional[int] = None
    activeSets: Optional[int] = None
    totalReps: Optional[int] = None
    minRespirationRate: Optional[float] = None
    maxRespirationRate: Optional[float] = None
    avgRespirationRate: Optional[float] = None
    trainingEffectLabel: Optional[str] = None
    activityTrainingLoad: Optional[int] = None
    avgFlow: Optional[float] = None
    avgGrit: Optional[float] = None
    minActivityLapDuration: float
    avgStress: Optional[float] = None
    startStress: Optional[int] = None
    endStress: Optional[int] = None
    differenceStress: Optional[int] = None
    maxStress: Optional[int] = None
    aerobicTrainingEffectMessage: Optional[str] = None
    anaerobicTrainingEffectMessage: Optional[str] = None
    splitSummaries: list
    hasSplits: bool
    moderateIntensityMinutes: Optional[int] = None
    vigorousIntensityMinutes: Optional[int] = None
    manualActivity: bool
    favorite: bool
    pr: bool
    autoCalcCalories: bool
    parent: bool
    atpActivity: bool
    decoDive: Optional[bool] = None
    elevationCorrected: bool
    purposeful: bool


class Device(BaseModel):
    userDeviceId: int
    userProfileNumber: int
    applicationNumber: int
    lastUsedDeviceApplicationKey: str
    lastUsedDeviceName: str
    lastUsedDeviceUploadTime: int
    imageUrl: str
    released: bool


class Weather(BaseModel):
    temp: int
    weatherTypeDTO: dict
    apparentTemp: int
    windGust: Optional[int] = None
    latitude: int
    dewPoint: int
    relativeHumidity: int
    windDirection: int
    issueDate: datetime
    windSpeed: int
    windDirectionCompassPoint: str
    longitude: float
    weatherStationDTO: dict


class HRZone(BaseModel):
    zoneNumber: int
    secsInZone: int
    zoneLowBoundary: int


class EventDTO(BaseModel):
    startTimeGMT: datetime
    startTimeGMTDoubleValue: int
    sectionTypeDTO: dict


class LapDTO(BaseModel):
    maxHR: int
    distance: int
    minElevation: float
    elevationGain: int
    averageRunCadence: float
    maxVerticalSpeed: float
    duration: float
    lengthDTOs: List[float]
    startLatitude: float
    startTimeGMT: datetime
    messageIndex: int
    averageMovingSpeed: float
    elevationLoss: int
    maxRunCadence: int
    lapIndex: int
    movingDuration: int
    averageSpeed: float
    maxSpeed: float
    calories: int
    strideLength: float
    endLatitude: float
    endLongitude: float
    averageHR: int
    startLongitude: float
    connectIQMeasurement: List[float]
    maxElevation: float
    elapsedDuration: int


class Split(BaseModel):
    activityId: int
    eventDTOs: List[EventDTO]
    lapDTOs: List[LapDTO]


class MetricDescriptors(BaseModel):
    key: str
    unit: dict
    metricsIndex: int


class Polyline(BaseModel):
    altitude: Optional[float] = None
    timerStart: bool
    distanceInMeters: Optional[float] = None
    cumulativeDescent: Optional[float] = None
    lon: Optional[float] = None
    timerStop: bool
    cumulativeAscent: Optional[float] = None
    distanceFromPreviousPoint: Optional[float] = None
    speed: Optional[int] = None
    valid: bool
    time: Optional[int] = None
    extendedCoordinate: bool
    lat: Optional[float] = None


class GeoPolylineDTO(BaseModel):
    endPoint: Polyline
    minLon: float
    maxLat: float
    minLat: float
    startPoint: Polyline
    polyline: List[Polyline]


class ActivityDetailMetric(BaseModel):
    metrics: List[Optional[float]]


class Details(BaseModel):
    activityId: int
    measurementCount: int
    metricsCount: int
    detailsAvailable: bool
    metricDescriptors: List[MetricDescriptors]
    geoPolylineDTO: GeoPolylineDTO
    activityDetailMetrics: List[ActivityDetailMetric]
    heartRateDTOs: Optional[List[float]] = None


class FullActivity(BaseModel):
    summary: Activity
    splits: Optional[Split] = None
    details: Optional[Details] = None
    weather: Optional[Weather] = None
    hr_zones: Optional[List[HRZone]] = None
