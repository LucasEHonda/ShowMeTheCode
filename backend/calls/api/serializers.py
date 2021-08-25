from rest_framework import serializers

from calls import models
from .adapters import CallAdapter


class CallsMyDetail(serializers.Serializer):
    origin = serializers.CharField(read_only=True)
    destiny = serializers.CharField(read_only=True)
    default_tariff = serializers.FloatField(read_only=True)
    talk_more_tariff = serializers.FloatField(read_only=True)
    plan = serializers.SerializerMethodField()
    minutes = serializers.IntegerField(read_only=True)

    def get_plan(self, obj):
        return CallAdapter.get_label(obj.plan)

class Calls(serializers.ModelSerializer):
    class Meta:
        model = models.Call
        fields = "__all__"

    def create(self, validated_data):
        plan = validated_data.get("plan")
        origin = validated_data.get("origin")
        destiny = validated_data.get("destiny")
        minutes = validated_data.get("minutes")

        default_tariff, talk_more_tariff = self._get_tariffs(
            plan, origin, destiny, minutes
        )
        call = models.Call.objects.create(
            origin=origin,
            destiny=destiny,
            talk_more_tariff=talk_more_tariff,
            default_tariff=default_tariff,
            plan=plan,
            minutes=minutes,
            user=self.context.get("request").user,
        )
        return self.serialize_instance(call)

    def _get_tariffs(self, plan, origin, destiny, minutes):
        if plan != models.Plan.DEFAULT:
            return (
                self._get_default_tariff(destiny, origin, minutes),
                self._get_talk_more_tariff(plan, destiny, origin, minutes),
            )
        return self._get_default_tariff(destiny, origin, minutes), 0

    def _get_default_tariff(self, destiny, origin, minutes):
        return self._get_tariff_by_ddd(destiny, origin) * minutes

    def _get_talk_more_tariff(self, plan, destiny, origin, minutes):
        if plan == models.Plan.TALK_MORE_LOW:
            excess_minutes_tariff = self._get_default_tariff(
                destiny, origin, minutes - 30
            )
            return (
                0
                if minutes <= 30
                else (excess_minutes_tariff + (0.10 * excess_minutes_tariff))
            )
        if plan == models.Plan.TALK_MORE_MEDIUM:
            excess_minutes_tariff = self._get_default_tariff(
                destiny, origin, minutes - 60
            )
            return (
                0
                if minutes <= 60
                else (excess_minutes_tariff + (0.10 * excess_minutes_tariff))
            )
        if plan == models.Plan.TALK_MORE_HIGH:
            excess_minutes_tariff = self._get_default_tariff(
                destiny, origin, minutes - 120
            )
            return (
                0
                if minutes <= 120
                else (excess_minutes_tariff + (0.10 * excess_minutes_tariff))
            )

    def _get_tariff_by_ddd(self, destiny, origin):
        if origin == "011":
            if destiny == "017":
                return 1.70
            if destiny == "018":
                return 0.90
        if origin == "016" and destiny == "011":
            return 2.90
        if origin == "017" and destiny == "011":
            return 2.70
        return 1.90

    def serialize_instance(self, instance):
        return CallsMyDetail(instance).data
