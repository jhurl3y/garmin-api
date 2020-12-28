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

class Rule(BaseModel):
    typeId: int
    typeKey: str

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
    rule: Rule
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
    moderateIntensityMinutes: int
    vigorousIntensityMinutes: int
    floorsAscendedInMeters: float
    floorsDescendedInMeters: float
    floorsAscended: float
    floorsDescended: float
    intensityMinutesGoal: int
    userFloorsAscendedGoal: int
    minHeartRate: int
    maxHeartRate: int
    restingHeartRate: int
    lastSevenDaysAvgRestingHeartRate: int
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
    heartRateValues: List[List[int]]